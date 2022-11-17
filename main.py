from sqlalchemy.orm import sessionmaker
from connect_to_db import connect_to_db, delete_table
from input_data import add_data
from query_row import query_row
from User import User
from env import DB_URL
def app():
    engine = connect_to_db(DB_URL)
    session = sessionmaker(bind=engine)()
    # CRUD part
    print("\n1. Add Data\n2. Fetch All Data\n3. Fetch particular row\n4. Update Particular Row\n5. Delete Particular Row\n6. Delete Table")
    option = int(input("Enter your choice:"))
    while option > 0 and option < 7:
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
            #session.commit()
            option = int(input("Enter your choice:"))
        elif option == 5:
            # First query for a particular row and then delete it. 
            option = int(input("Enter your choice:"))
        elif option == 6:
            # Delete the whole table
            delete_table(DB_URL)
            option = int(input("Press 0 to exit."))
    session.close()

if __name__ == '__main__':
    app()