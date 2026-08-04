from DB import conn, cursor

def add():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    cursor.execute(
        "INSERT INTO student(name, age) VALUES (%s, %s)",
        (name, age)
    )

    conn.commit()
    print("Saved")


def get_stud():
    cursor.execute("select * from student")
    row=cursor.fetchall()
    print("Student details are:")
    for r in row:
        print(r)

def search():
    
    id=int(input("enter id: "))
    cursor.execute("Select * from student where id = %s",(id))
    row=cursor.fetchone()
    print(row)



def age():
    cursor.execute("select  name from student where age>5")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

def search_name():
    cursor.execute(
        "SELECT id, age FROM student WHERE name LIKE '%a%'"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)



def even_id():
    cursor.execute("SELECT * FROM student WHERE id % 2 = 0")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def count_records():
    
    cursor.execute("select count(*) from student")
    count=cursor.fetchone()
    print("count:",count)

def max_age():
    cursor.execute("select name from student order by age DESC limit 1")
    print(cursor.fetchone())
    