from User import User

def update_row(session):
    row_count = ''
    user_name = input("Enter the record name for filter:")
    param = input("Enter the update param:")
    updatedVal = input("Enter the updated value:")
    if param == 'name':
        row_count = session.query(User).filter(User.name == user_name).update({User.name: updatedVal},synchronize_session='evaluate')
    elif param == 'gender':
        row_count = session.query(User).filter(User.name == user_name).update({User.gender: updatedVal},synchronize_session='evaluate')
    elif param == 'age':
        row_count = session.query(User).filter(User.name == user_name).update({User.age: updatedVal},synchronize_session='evaluate')
    elif param == 'email':
        row_count = session.query(User).filter(User.name == user_name).update({User.email: updatedVal},synchronize_session='evaluate')
    elif param == 'salary':
        row_count = session.query(User).filter(User.name == user_name).update({User.salary: updatedVal},synchronize_session='evaluate')
    elif param == 'phone_number':
        row_count = session.query(User).filter(User.name == user_name).update({User.phone_number: updatedVal},synchronize_session='evaluate')
    return row_count