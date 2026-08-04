import sqlite3

conn=sqlite3.connect("LINKCODE.db")
print("database connected")

#cursor object -->execute("Table create syntax")
cursor=conn.cursor()

#create table 
cursor.execute("""
create table if not exists student(
id int ptimary key,
name text not null,
age int 
)
""")


#mannual
#print("table created")

#cursor.execute(
#    "INSERT INTO student(id, name, age) VALUES (?, ?, ?)",
#    (1, "swanandi", 20)
#)

#conn.commit()
#print("Data inserted")








#update()
#view_all_stud()
#delete()
