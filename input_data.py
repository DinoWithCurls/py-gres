from User import User
import datetime
def add_data():
    user_data = {}
    user_data['name'] = input("Enter the name:")
    user_data['email'] = input("Enter the email:")
    user_data['phone_number'] = input("Enter the phone number:")
    user_data['age'] = int(input("Enter the age:"))
    user_data['gender'] = input("Enter the gender:")
    user_data['salary'] = int(input("Enter the salary:"))
    print("Date of Birth")
    dob_y = int(input("Enter the DOB year:"))
    dob_m = int(input("Enter the DOB month:"))
    dob_d = int(input("Enter the DOB date:"))
    dob = datetime.date(dob_y, dob_m, dob_d)
    user_data['date_of_birth'] = dob
    user_data['created_date'] = datetime.datetime.now()
    user = User(
        name=user_data["name"],
        email=user_data["email"],
        phone_number=user_data["phone_number"],
        age=user_data["age"],
        gender=user_data["gender"],
        salary=user_data["salary"],
        date_of_birth=user_data["date_of_birth"],
        created_date=user_data["created_date"]
    )
    return user
    