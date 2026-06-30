import json
import os

FILE_NAME = "Student.json"
#-------JSON Function-------
def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
     with open(FILE_NAME, "r") as file:
        return json.load(file)
     
    except:
        return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)
#-------Validation Function-------
def name_validation():
    while True:
        name = input("Enter Name: ")

        if name.replace(" ", "").isalpha():
            return name

        else:
            print("Name should contain only alphabets!")
def get_valid_age():
    while True:
        age = input("Enter Age: ")

        if age.isdigit() and 1 <= int(age) <= 100:
            return age

        print("Invalid Age! Please enter a valid number.")


def get_valid_email():
    while True:
        email = input("Enter Email: ")

        if "@" in email and "." in email:
            return email

        print("Invalid Email!")
def get_valid_phone():
    while True:
        phone = input("Enter Phone Number: ")

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Phone number must contain exactly 10 digits.")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        students = load_students()
        if students:
         new_id = max(student["id"] for student in students) + 1
        else:
         new_id = 1

        student = {
     "id": new_id,
     "name": name_validation().title(),
     "age": get_valid_age(),
     "course": input("Enter Course: "),
     "email" : get_valid_email(),
     "phone" : get_valid_phone()
     }

        students.append(student)

        save_students(students)

        print("Student Added Successfully!")

    elif choice == "2":
        students = load_students()

        if len(students) == 0:
         print("No students found.")

        else:
         print("\n===== Student List =====")

         for student in students:
          print("----------------------------")
          print("ID     :", student["id"])
          print("Name   :", student["name"])
          print("Age    :", student["age"])
          print("Course :", student["course"])
          print("Email  :", student["email"])
          print("Phone  :", student["phone"])
        

    elif choice == "3":
        students = load_students()

        try:
            search_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        found = False
        for student in students:
          if student["id"] == search_id:
           print("\n===== Student Found =====")
           print("ID     :", student["id"])
           print("Name   :", student["name"])
           print("Age    :", student["age"])
           print("Course :", student["course"])
           print("Email  :", student["email"])
           print("Phone  :", student["phone"])
           found = True
           break

        if not found:
           print("Student not found!")

    elif choice == "4":
        students = load_students()

        try:
            update_id = int(input("Enter Student ID to Update: "))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        found = False

        for student in students:
          if student["id"] == update_id:
           student["name"] = name_validation().title()
           student["age"] = get_valid_age()
           student["course"] = input("Enter New Course: ")
           student["email"] = get_valid_email()
           student["phone"] = get_valid_phone()

           save_students(students)

           print("Student Updated Successfully!")
           found = True
           break

        if not found:
         print("Student not found!")

    elif choice == "5":
        students = load_students()

        try:
            delete_id = int(input("Enter Student ID to Delete: "))
        except ValueError:
            print("Invalid ID! Please enter a number.")
            continue

        found = False

        for student in students:
         if student["id"] == delete_id:
          students.remove(student)
          save_students(students)
          print("Student Deleted Successfully!")
          found = True
          break

        if not found:
         print("Student not found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Please try again.")
