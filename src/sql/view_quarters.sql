CREATE VIEW globant_challenge.view_quarters AS
select d.department_name, j.job_name, COUNT(Q1) as Q1, COUNT(Q2)as Q2, COUNT(Q3) as Q3, COUNT(Q4) as Q4 from (
SELECT department_id, job_id, MONTH(hire_datetime) as Q1, null as Q2, null as Q3, null as Q4  FROM globant_challenge.hired_employees
where MONTH(hire_datetime) BETWEEN 1 and 3 and year(hire_datetime) = 2021
UNION
SELECT department_id, job_id, null as Q1, MONTH(hire_datetime) as Q2, null as Q3, null as Q4  FROM globant_challenge.hired_employees
where MONTH(hire_datetime) BETWEEN 4 and 6 and year(hire_datetime) = 2021
UNION
SELECT department_id, job_id, null as Q1, null as Q2, MONTH(hire_datetime) as Q3, null as Q4  FROM globant_challenge.hired_employees
where MONTH(hire_datetime) BETWEEN 7 and 9 and year(hire_datetime) = 2021
UNION
SELECT department_id, job_id,null as Q1, null as Q2, null as Q3, MONTH(hire_datetime) as Q4  FROM globant_challenge.hired_employees
where MONTH(hire_datetime) BETWEEN 10 and 12 and year(hire_datetime) = 2021 ) as temp1
inner join globant_challenge.departments d  on temp1.department_id = d.id
inner join globant_challenge.jobs j on temp1.job_id = j.id
group by temp1.department_id, temp1.job_id
order by d.department_name asc, j.job_name asc;