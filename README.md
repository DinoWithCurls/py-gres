## Problem Statement
Technologies: Python3.8+, Postgresql, https://www.sqlalchemy.org/
Description:
1. Install postgres
2. Create below table on Postgresql
Table Name: users

| Column Name   | Type      |
|---------------|-----------|
| name          | Text      |
| email         | Text      |
| phone_number  | Text      |
| age           | Number    |
| gender        | Text      |
| salary        | Number    |
| date_of_birth | Timestamp |
| created_date  | Timestamp |


3. Write python code to insert into this table
4. Write python code to update row in this table
5. Write python code to find row in this table
6. Write python code to delete row in this table

## Solution

1. Clone the project
2. cd into the project directory
3. Create a new virtual environment and activate it
```
virtualenv env && source env/bin/activate
```
4. Run the following command (NOTE: psycopg2-binary will only work properly inside a virtual environment)
```
pip install -r requirements.txt
```
3. Create a file by the name env.py in the root, and add the following values:
```
DB_NAME = "<name of your db>"
DB_USER = "<your username for the db>"
DB_PASS = "<password for db>"
CONN_URL = "<your host IP, use localhost for default value>"
CONN_PORT = "<your host port, use 5432 for default value>"
DB_URL = DB_URL = "postgresql+psycopg2://" + DB_USER + ":" + DB_PASS + "@" + CONN_URL + CONN_PORT + "/" + DB_NAME
```
4. Run main.py

