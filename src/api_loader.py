import csv
import io
import flask
from flask import request, render_template
from database import db_session
from models import bulk_process, hired_employees, hired_by_quarter
from flask import Response


ALLOWED_EXTENSIONS = {'csv'}

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home():
    return render_template("menu.html")

@app.route('/dasboard/hired_employees', methods=['GET'])
def hired_employees_api():
    data = hired_employees(db_session)
    return render_template("hired_employees.html", data=data)

@app.route('/dasboard/hired_by_quarter', methods=['GET'])
def hired_by_quarter_api():
    data = hired_by_quarter(db_session)
    return render_template("hired_by_quarter.html", data=data)

def process_file(file, entity):
    reader_list = csv.reader(io.StringIO(file.read().decode("utf-8")), delimiter=',')
    sender_bulk = [row for row in reader_list]

    if len(sender_bulk) == 0:
        return Response("Bad request, no data found", status=400)
    elif type(sender_bulk) != list:
        return Response("Bad request, data must be a list", status=400)
    
    if len(sender_bulk) > 1000:
        for r in range(0, len(sender_bulk), 1000):
            result = bulk_process(sender_bulk[r:r+1000], db_session, entity)
    else:
        result = bulk_process(sender_bulk, db_session, entity)
    return result
    

@app.route('/file/v1/<entity>', methods=['POST'])
def upload_file(entity):
    if request.method == 'POST':
        if entity not in ('departments', 'jobs', 'hired_employees'):
               return Response("Bad request", status=404)
        if 'file' not in request.files:
            return Response('No file part', status=404)
        file = request.files['file']
        if file.filename == '':
            return Response('No selected file', status=404)
    
        if file and allowed_file(file.filename):
            return process_file(file, entity)
    return Response("Bad request", status=404)

@app.route('/<entity>/v1/bulk', methods=['POST'])
def deparments_bulk_insert(entity):
    request_data = request.get_json()
    if entity not in ('departments', 'jobs', 'hired_employees'):
        return Response("Bad request", status=404)

    if len(request_data) > 1000:
        return Response("Payload too large", status=413)
    elif len(request_data) == 0:
        return Response("Bad request, no data found", status=400)
    elif type(request_data) != list:
        return Response("Bad request, data must be a list", status=400)

    return bulk_process(request_data, db_session, entity)


app.run()
