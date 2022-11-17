from User import User

def delete_row(session):
    row_count = ''
    colName = input("Enter the column name for filter:")
    param = input("Enter the row value to be deleted:")
    if colName == 'name':
        row_count = session.query(User).filter(User.name == param).delete(synchronize_session='evaluate')
    elif colName == 'gender':
        row_count = session.query(User).filter(User.gender == param).delete(synchronize_session='evaluate')
    elif colName == 'age':
        row_count = session.query(User).filter(User.age == param).delete(synchronize_session='evaluate')
    elif colName == 'email':
        row_count = session.query(User).filter(User.email == param).delete(synchronize_session='evaluate')
    elif colName == 'salary':
        row_count = session.query(User).filter(User.salary  == param).delete(synchronize_session='evaluate')
    elif colName == 'phone_number':
        row_count = session.query(User).filter(User.phone_number == param).delete(synchronize_session='evaluate')
    return row_count