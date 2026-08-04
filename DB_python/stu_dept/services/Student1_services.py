from models.student1 import student1
from db import conn,cursor

def add_student():
    name=input("enter name of student:")
    age=int(input("enter age "))
    email=input("enter email Id")
    dept_is=int(input("enter department id"))
    query = "Insert into student1 (name,age,email,dept_is) values(%s,%s,%s,%s)"
    values=(name,age,email,dept_is)
    cursor.execute(query,values)
    conn.commit()
    print("student data added sucessfully")

def read_student():
    query = "SELECT * FROM student1"

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)


def update_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    email = input("Enter new email: ")
    dept_is = int(input("Enter new department ID: "))

    query = """
    UPDATE student1
    SET name=%s, age=%s, email=%s, dept_is=%s
    WHERE student_id=%s
    """

    values = (name, age, email, dept_is, student_id)

    cursor.execute(query, values)
    conn.commit()

    print("Student updated successfully")


def search_student():
    student_id = int(input("Enter student ID: "))

    query = "SELECT * FROM student1 WHERE student_id=%s"

    cursor.execute(query, (student_id,))

    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print("Student not found")



def view_student_department():
    query = """
    SELECT s.name, d.dep_name
    FROM student1 s
    JOIN department d
    ON s.dept_is = d.dep_id
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    print("Student Name\tDepartment")
    for row in rows:
        print(f"{row[0]}\t\t{row[1]}")