import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="learn-python"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = '123 Main St'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted.")
