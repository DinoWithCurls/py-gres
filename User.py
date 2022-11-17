from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime

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
    date_of_birth = Column(Date)
    created_date = Column(DateTime)
    def __repr__(self):
        return "<User(name='{}', email='{}', phone_number={}, age={}, gender={}, salary={}, date_of_birth={}, created_date={})>"\
                .format(self.name, self.email, self.phone_number, self.age, self.gender, self.salary, self.date_of_birth, self.created_date)