import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="learn-python"
)

mycursor = mydb.cursor()

sql = "SELECT COUNT(*) FROM customers"
mycursor.execute(sql)

result = mycursor.fetchone()

print("Total customers:", result[0])
