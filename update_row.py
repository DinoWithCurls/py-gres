from User import User

def update_row(session):
    row = ''
    user_name = input("Enter the record name for filter:")
    param = input("Enter the update param:")
    updatedVal = input("Enter the updated value:")
    if param == 'name':
        row = session.query(User).filter(User.name == user_name).update({User.name: updatedVal},synchronize_session='evaluate')
    elif param == 'gender':
        row = session.query(User).filter(User.name == user_name).update({User.gender: updatedVal},synchronize_session='evaluate')
    elif param == 'age':
        row = session.query(User).filter(User.name == user_name).update({User.age: updatedVal},synchronize_session='evaluate')
    elif param == 'email':
        row = session.query(User).filter(User.name == user_name).update({User.email: updatedVal},synchronize_session='evaluate')
    elif param == 'salary':
        row = session.query(User).filter(User.name == user_name).update({User.salary: updatedVal},synchronize_session='evaluate')
    elif param == 'phone_number':
        row = session.query(User).filter(User.name == user_name).update({User.phone_number: updatedVal},synchronize_session='evaluate')
    return row