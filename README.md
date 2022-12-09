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
4. Create a file called env.py in the root, and add the following line into it:
```
DB_URL = "postgresql+psycopg2://" + DB_USER + ":" + DB_PASS + "@db" + "/" + DB_NAME
```
4. Install Docker in your system and start the app
5. Run the following command
```
docker pull postgres
```
6. Run the files runPostgres.sh and runServer.sh in different terminal tabs, after adding your own password in runPostgres.sh
7. Run the following commands in another terminal:
```
docker-compose up --build
docker network connect py-gres_default db
docker network connect py-gres_default web
```
8. Access pgAdmin4 on the postgres url, and create the table with the schema provided above, else all endpoints other than "/" will throw "NO TABLE" error.

9. Test the following endpoints on POSTMAN with their respective methods:

| ENDPOINT        | METHOD | USE                           |
|-----------------|--------|-------------------------------|
| /               | GET    | Root                          |
| /users          | GET    | Get all data present in table |
| /user           | POST   | Enter data into the table     |
| /user/{user_id} | GET    | Get a single row              |
| /user/{user_id} | PUT    | Update a single row           |
| /user/{user_id} | DELETE | Delete a single row           |

