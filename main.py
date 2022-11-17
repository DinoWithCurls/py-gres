from sqlalchemy.orm import sessionmaker
from connect_to_db import connect_to_db
from input_data import add_data
from query_row import query_row
from update_row import update_row
from delete_row import delete_row
from User import User
from env import DB_URL
def app():
    engine = connect_to_db(DB_URL)
    session = sessionmaker(bind=engine)()
    # CRUD part
    print("The columns that can be currently queried are: name\tgender\tphone_number\temail\tage\tsalary")
    print("Only == operator is being used for filtering at the moment. Will add support for more operators and more columns.")
    print("\n1. Add Data\n2. Fetch All Data\n3. Fetch particular row\n4. Update Particular Row\n5. Delete Particular Row")
    option = int(input("Enter your choice:"))
    while option > 0 and option < 5:
        if option == 1:
            # Take data as user input and add it into table
            user = add_data()
            session.add(user)
            session.commit()
            option = int(input("Enter your choice:"))
        elif option == 2:
            # Query and get the whole table
            print(session.query(User).all())
            option = int(input("Enter your choice:"))
        elif option == 3:    
            # Query for a particular row
            returnedRows = query_row(session)
            for row in returnedRows:
                print(row)
            option = int(input("Enter your choice:"))
        elif option == 4:
            # First query for a particular row and then update it. Return the updated row
            row_count = update_row(session)
            print("Rows updated", row_count)
            session.commit()
            updated_row = query_row(session)
            print(updated_row)
            option = int(input("Enter your choice:"))
        elif option == 5:
            # First query for a particular row and then delete it.
            row_count = delete_row(session)
            print(row_count)
            print(session.query(User).all())
            session.commit()
            option = int(input("Enter your choice:"))
    session.commit()
    session.close()

if __name__ == '__main__':
    app()