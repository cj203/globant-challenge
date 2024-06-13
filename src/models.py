from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from flask import Response
from dateutil import parser 

Base = declarative_base()

class HiredEmployees(Base):
    __tablename__ = "hired_employees"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    hire_datetime = Column(DateTime, nullable=False)
    department_id = Column(Integer(), nullable=False)
    job_id = Column(Integer(), nullable=False)

    def __init__(self,
                 id=None,
                 name=None, 
                 hire_datetime=None, 
                 department_id=None, 
                 job_id=None):
        self.id = id
        self.name = name
        self.hire_datetime = hire_datetime
        self.department_id = department_id
        self.job_id = job_id


class Departments(Base):
    __tablename__ = "departments"
    id = Column(Integer(), primary_key=True)
    deparment_name = Column(String(100), nullable=False)

    def __init__(self, id=None, deparment_name=None):
        self.id = id
        self.deparment_name = deparment_name
    

class Jobs(Base):
    __tablename__ = "jobs"
    id = Column(Integer(), primary_key=True)
    job_name = Column(String(100), nullable=False)

    def __init__(self, id=None, job_name=None):
        self.id = id
        self.job_name = job_name

    def __repr__(self):
        return f'<job_name {self.job_name!r}>'


def departments_bulk_execute(n, session, entity):
    try:
        print(entity)
        if entity == "departments":
            print("departments")
            session.execute(
                insert(Departments),
                _deparments_list_create(n),
            )
        elif entity == "jobs":
            print("jobs")
            session.execute(
                insert(Jobs),
                _jobs_list_create(n),
            )
        elif entity == "hired_employees":
            print("hired_employees")
            session.execute(
                insert(HiredEmployees),
                _hired_employees_list_create(n),
            )
        session.commit()
        return Response("Successfull", status=200)
    except IntegrityError as e:
        print(e)
        return Response("Duplicate error", status=409)

def _hired_employees_list_create(data):
    return [
                {
                    "id": int(data[i][0]),
                    "name": data[i][1],
                    "hire_datetime": parser.parse(data[i][2]),
                    "department_id": int(data[i][3]),
                    "job_id": int(data[i][4]),
                }
                for i in range(len(data)) if data[i][1] and data[i][2] and data[i][4]
            ]

def _deparments_list_create(data):
    return [
                {
                    "id": int(data[i][0]),
                    "deparment_name": data[i][1],
                }
                for i in range(len(data))
            ]

def _jobs_list_create(data):
    return [
                {
                    "id": int(data[i][0]),
                    "job_name": data[i][1],
                }
                for i in range(len(data))
            ]