import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="learn-python"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = '123 Main St'"
mycursor.execute(sql)

result = mycursor.fetchall()

for row in result:
  print(row)
