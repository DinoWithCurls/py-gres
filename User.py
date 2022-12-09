from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
Base = declarative_base()
# Create a class for the table definition
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    age = Column(Integer)
    gender = Column(String)
    salary = Column(Integer)
    created_date = Column(DateTime(timezone=True), server_default=func.now())