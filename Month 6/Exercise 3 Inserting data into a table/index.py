import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="learn-python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John Doe", "123 Main St")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
