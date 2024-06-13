import flask
from flask import request
from database import db_session
from models import departments_bulk_execute
from flask import Response


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
 return '''<h1>Home</h1>'''

@app.route('/deparments/', methods=['POST'])
def deparments_insert():
   request_data = request.get_json()
   print(request_data)
   id = request_data['id']
   deparment_name = request_data['deparment_name']
#    d = Departments(id, deparment_name)
#    db_session.add(d)
#    db_session.commit()
   return '''
           The language value is: {}
           The framework value is: {}'''.format(id, deparment_name)

# GET requests will be blocked
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

   return departments_bulk_execute(request_data, db_session, entity)


app.run()






# print(db_session.query(Jobs).all())
