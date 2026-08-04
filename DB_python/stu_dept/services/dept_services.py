from models.dept import dept
from db import conn,cursor

def add_dept():
    dep_name=input("enter ddept name:")
    d=dept(dep_name)
    query="Insert into department (dep_name) values(%s)"
    values = (d.dep_name,)
    cursor.execute(query,values)
    conn.commit()
    print("department added sucessfully")

def update():
    dept_is=int(input("enter department id"))
    dep_name=input("enter dept name:")
    d=dept(dep_name)
    query = "update department  set dep_name = %s where dept_is=%s"
    values=(d.dep_name,dept_is)
    cursor.execute(query,values)
    conn.commit()
    print("department updated sucessfully ")

def read_dept():
    query = "SELECT * FROM department"

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

def delete_dept():
    dept_is = int(input("Enter department ID to delete: "))
    

    query = "DELETE FROM department WHERE dept_is = %s"
    values = (dept_is,)

    cursor.execute(query, values)
    conn.commit()

    print("Department deleted successfully")


def search_dept():
    dept_is = int(input("Enter department ID: "))

    query = "SELECT * FROM department WHERE dept_is = %s"
    values = (dept_is,)

    cursor.execute(query, values)

    row = cursor.fetchone()

    if row:
        print("Department Found:")
        print(row)
    else:
        print("Department Not Found")








