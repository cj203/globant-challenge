create database globant_challenge;
use globant_challenge;


CREATE TABLE hired_employees (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    hire_datetime DATETIME NOT NULL,
    department_id INT NOT NULL,
    job_id INT NOT NULL
);

CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    job_name VARCHAR(100) NOT NULL
);

CREATE TABLE deparments (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    deparment_name VARCHAR(100) NOT NULL
);