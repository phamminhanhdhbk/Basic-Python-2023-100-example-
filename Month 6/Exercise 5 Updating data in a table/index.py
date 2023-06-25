import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="learn-python"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = '456 Oak St' WHERE name = 'John Doe'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) updated.")
