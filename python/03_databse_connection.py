import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_db"
)
if connection.is_connected():
    print("MYSQL connection sucessful!")

connection.close()