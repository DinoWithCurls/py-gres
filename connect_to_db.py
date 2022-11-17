import sqlalchemy
from sqlalchemy import create_engine
from User import Base
# check if the db already contains the table, else create a new table with the name users
def connect_to_db(DB_URL):
    engine = create_engine(DB_URL)
    inspectDB = sqlalchemy.inspect(engine)
    ret = inspectDB.dialect.has_table(engine.connect(), 'users')
    if(ret == False):
        Base.metadata.create_all(engine)
    print("Table Initialised!")
    return engine