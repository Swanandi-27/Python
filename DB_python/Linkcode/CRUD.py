from db import conn,cursor
def add_stud():
    id=int(input("enter id:"))
    name=input("enter name:")
    age=int(input("enter your age:"))
    cursor.execute("Insert into student(id,name,age) values(?,?,?)",(id,name,age))
    conn.commit()
    print("data Inserted")


def view_all_stud():
    cursor.execute("select * from student")
    rows=cursor.fetchall()
    print(rows)

#only names
#for i in rows:
#    print(i[1])

def Search():
    id=int(input("enter id: "))
    cursor.execute("Select * from student where id =?",(id))
    row=cursor.fetchone()
    print(row)

def update():
    id = int(input("Enter ID: "))

    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    for row in rows:
        if row[0] == id:
            name = input("Enter name: ")
            age = int(input("Enter age: "))

            cursor.execute(
                "UPDATE student SET name = ?, age = ? WHERE id = ?",
                (name, age, id)
            )

            conn.commit()
            print("Record updated successfully")
            break
    else:
        print("ID not found") 

def delete():
    id = int(input("Enter ID: "))

    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()

    for row in rows:
        if row[0] == id:
            cursor.execute("DELETE FROM student WHERE id = ?", (id,))
            conn.commit()
            print("Record deleted successfully")
            break
    else:
        print("ID not found")
