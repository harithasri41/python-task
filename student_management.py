from student import Student
from database import Database

db = Database()

try:
    while True:

        print("STudent Management SYSTEM")
        print("1.Add Student")
        print("2.View All Students:")
        print("3. Search student:")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Enter your choice:")

        if choice =="1":

            name = input("Enter student Name:")
            age = int(input("Enter Student Age:"))
            email = input("Enter Student Email")

            Student = Student(name,age,email)

            db.add_student(Student)

        elif choice == "2":
            db.view_students()

        elif choice =="3":

            student_id = int(input("Enter Student ID:"))

            db.search_student(student_id)

        elif choice == "4":

             student_id = int(input("Enter Student ID:"))

             name = input("Enter New Name: ")
             age = int(input("Enter New Age:"))
             email = input("Enter New email:")
             db.update_student(student_id,name,ag,email)
        elif choice =="5":
            student_id = int(input("Enter student ID:"))
            db.delete(student_id)

        elif choice =="6":

            print("Thank you for using student management system")
            break
        else:
            print("Invalid choice:please try again")
finally:
   db.close_connection()

