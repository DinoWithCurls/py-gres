from User import User

def query_row(session):
    row = ''
    colName = input("Enter the column name for filter:")
    param = input("Enter the query param:")
    if colName == 'name':
        row = session.query(User).filter(User.name == param).all()
    elif colName == 'gender':
        row = session.query(User).filter(User.gender == param).all()
    elif colName == 'age':
        row = session.query(User).filter(User.age == param).all()
    elif colName == 'email':
        row = session.query(User).filter(User.email == param).all()
    elif colName == 'salary':
        row = session.query(User).filter(User.salary  == param).all()
    elif colName == 'phone_number':
        row = session.query(User).filter(User.phone_number == param).all()
    return row
