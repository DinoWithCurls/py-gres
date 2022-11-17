from User import User


def query_row(session):
    row = ''
    print("The columns that can be currently queried are: name\tgender")
    colName = input("Enter the column name for filter:")
    param = input("Enter the query param:")
    print("Only == operator is being used for filtering at the moment. Will add support for more operators and more columns.")
    if colName == 'name':
        row = session.query(User).filter(User.name == param).all()
    elif colName == 'gender':
        row = session.query(User).filter(User.gender == param).all()
    return row
