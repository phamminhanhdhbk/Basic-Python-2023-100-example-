import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="learn-python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

result = mycursor.fetchall()

for row in result:
  print(row)
