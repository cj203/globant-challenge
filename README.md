# Globant Challenge


This API upload file to a MySQL database, also can upload bulk of data
has been develop with Python, Flask and MySQL.

## Features

- Can upload file up to 16MB
- Can received data up to 1000 rows
- Have a Dashboard

## Tech

Dillinger uses a number of open source projects to work properly:

- [sqlalchemy] - The Python SQL Toolkit and Object Relational Mapper
- [flask] - Flask is a lightweight WSGI web application framework
- [requests] - Requests is a simple, yet elegant, HTTP library.
- [mysql] - Relational Database.
- [dillinger] - Markdown parser done right. Fast and easy to extend.

## Installation

Install the dependencies and devDependencies and start the server.

Clone the repo into your workspace
```sh
cd workspace
git clone https://github.com/cj203/globant-challenge.git
```

Install dependencies:
```sh
cd globant-challenge
git checkout develop
pip install -r requirements.txt
```
For run, you need two terminal, one to run the service and another one to send data.

For set up the service:
```sh
cd src
python3 api_loader.py
```
You can see somethings like that:
```sh
 * Serving Flask app 'api_loader'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 861-544-462
```

In another terminal, you can run this request:

You need pass two parametters: -t (`test`) and -f (`file`)
```
-t, options:
    1 - Send bulk data from a file
    2 - Send file
-f, options: the file name
    'departments', 'jobs', 'hired_employees'
```

```sh
python3 data_sender.py -t 2 -f jobs
python3 data_sender.py -t 1 -f departments
python3 data_sender.py -t 1
```

## SQL questions

http://127.0.0.1:5000/dasboard/hired_employees
http://127.0.0.1:5000/dasboard/hired_by_quarter

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [sqlalchemy]: <https://docs.sqlalchemy.org/en/20/>
   [flask]: <https://flask.palletsprojects.com/en/3.0.x/>
   [requests]: <https://pypi.org/project/requests/>
   [mysql]: <https://dev.mysql.com/downloads/>
   [dillinger]: <https://dillinger.io/>
