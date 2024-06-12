from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HiredEmployees(db.Model):
    __tablename__ = "hired_employees"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    hire_datetime = db.Column(db.Datetime, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)


class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deparment_name = db.Column(db.String(100), nullable=False)


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(100), nullable=False)
