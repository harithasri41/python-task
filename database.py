import mysql.connector
class Database:
    def __init__(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Juvarya@2020",
            database="student_db"
        )
        self.cursor = self.connection.cursor()
        print("Database connected Successfully")
         # CREATE - Add Student
    def add_student(self, student):

        query = """
        INSERT INTO students (name, age, email)
        VALUES (%s, %s, %s)
        """

        values = (student.name, student.age, student.email)

        self.cursor.execute(query, values)
        self.connection.commit()

        print("Student Added Successfully!")

    # READ - View All Students
    def view_students(self):

        query = "SELECT * FROM students"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        if not records:
            print("No student records found!")
        else:
            for student in records:
                print(student)

    # READ - Search Student
    def search_student(self, student_id):

        query = "SELECT * FROM students WHERE id = %s"

        self.cursor.execute(query, (student_id,))

        record = self.cursor.fetchone()

        if record:
            print("Student Details:", record)
        else:
            print("Student Not Found!")

    # UPDATE - Edit Student
    def update_student(self, student_id, name, age, email):

        query = """
        UPDATE students
        SET name = %s, age = %s, email = %s
        WHERE id = %s
        """

        values = (name, age, email, student_id)

        self.cursor.execute(query, values)
        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("Student Updated Successfully!")
        else:
            print("Student Not Found!")

    # DELETE - Remove Student
    def delete_student(self, student_id):

        query = "DELETE FROM students WHERE id = %s"

        self.cursor.execute(query, (student_id,))
        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    # Close Database
    def close_connection(self):

        self.cursor.close()
        self.connection.close()

        print("Database Connection Closed!")
