from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from flask import Response
from dateutil import parser 
from sqlalchemy.sql import text

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


def bulk_process(n, session, entity):
    try:
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
                for i in range(len(data))
                if data[i][1] and data[i][2] and data[i][3] and data[i][4]
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

def hired_employees(session):
    query = text("""
        select d.id, d.department_name, hired from
        (
            SELECT AVG(dd.hired) as median_val
            FROM (
            select department_id, COUNT(*) hired, @rownum:=@rownum+1 as `row_number`, @total_rows:=@rownum 
            from globant_challenge.hired_employees, (SELECT @rownum:=0) r
            where year(hire_datetime) = 2021
            group by department_id
            ORDER BY hired
            ) as dd
            WHERE dd.row_number IN ( FLOOR((@total_rows+1)/2), FLOOR((@total_rows+2)/2) )
        ) temp, (
            select department_id, COUNT(*) hired
            from globant_challenge.hired_employees e
            where year(hire_datetime) = 2021
            group by department_id
        ) as temp2
        inner join globant_challenge.departments as d on temp2.department_id = d.id
        where temp2.hired > temp.median_val
        order by temp2.hired DESC;""")
    return session.execute(query).all()

def hired_by_quarter(session):
    query = text("""Select * from globant_challenge.view_quarters limit 300""")
    return session.execute(query).all()