import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root", 
    password="swanandi",
    database="python45"
)

print("Database Connected Sucessfully")

cursor=conn.cursor()