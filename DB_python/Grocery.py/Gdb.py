import sqlite3

conn=sqlite3.connect("Grocery.db")
print("database created sucessfully")
cursor=conn.cursor()

cursor.execute("""create table if not exists 
product(
product_id int primary key,
Name text not null,
brand text not null,
mfg_date text,
exp_date text,
quantity int,
price int
)
""")
print("table created sucessfully")

