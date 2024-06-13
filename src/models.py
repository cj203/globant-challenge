from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HiredEmployees(Base):
    __tablename__ = "hired_employees"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    hire_datetime = Column(DateTime, nullable=False)
    department_id = Column(Integer(), nullable=False)
    job_id = Column(Integer(), nullable=False)

    def __init__(self, name=None, 
                 hire_datetime=None, 
                 department_id=None, 
                 job_id=None):
        self.name = name
        self.hire_datetime = hire_datetime
        self.department_id = department_id
        self.job_id = job_id


class Departments(Base):
    __tablename__ = "departments"
    id = Column(Integer(), primary_key=True)
    deparment_name = Column(String(100), nullable=False)

    def __init__(self, deparment_name=None):
        self.deparment_name = deparment_name


class Jobs(Base):
    __tablename__ = "jobs"
    id = Column(Integer(), primary_key=True)
    job_name = Column(String(100), nullable=False)

    def __init__(self, job_name=None):
        self.job_name = job_name

    def __repr__(self):
        return f'<job_name {self.job_name!r}>'
