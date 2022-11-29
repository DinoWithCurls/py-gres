from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str 
    phone_number: str 
    age: int 
    gender: str 
    salary: int

    class Config: 
        orm_mode = True