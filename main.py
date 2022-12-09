import uvicorn
from fastapi import FastAPI 
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import User as UserSchema
from schema import User
from User import User as UserModel
from env import DB_URL

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

@app.get("/")
async def root():
    return {"message": "CRUD operations in PostgreSQL using Python FastAPI"}

# Take data as user input and add it into table
@app.post('/user/', response_model=UserSchema)
async def adduser(user: UserSchema):
    db_user = UserModel(
        name=user.name,
        email=user.email,
        phone_number=user.phone_number,
        age=user.age,
        gender=user.gender,
        salary=user.salary,
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user

# Get all users
@app.get('/users/')
async def allusers():
    users = db.session.query(UserModel).all()
    return users

# Get one user
@app.get('/user/{user_id}', response_model=UserSchema)
async def oneuser(user_id: int):
    user = db.session.query(UserModel).filter(UserModel.id == user_id).first()
    return user

# Update one user
@app.put('/user/{user_id}', response_model=UserSchema)
async def updateuser(user_id: int, updateVal: UserSchema):
    #user = db.session.query(UserModel).filter(UserModel.id == user_id).all()
    updated_row = db.session.query(UserModel).filter(UserModel.id == user_id).update({
        name:updateVal.name,
        email: updateVal.email,
        phone_number: updateVal.phone_number,
        age: updateVal.age,
        gender:updateVal.gender,
        salary: updateVal.salary
    })
    db.session.commit()
    updatedUser = db.session.query(UserModel).filter(UserModel.id == user_id).first()
    return updatedUser

# Delete one user
@app.delete('/user/{user_id}', response_model=list[UserSchema])
async def deleteuser(user_id: int):
    row_affected = db.session.query(UserModel).filter(UserModel.id == user_id).delete()
    db.session.commit()
    updated_user_list = db.session.query(UserModel).all()
    return updated_user_list


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)