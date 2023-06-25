import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="learn-python"
)

mycursor = mydb.cursor()

# Tạo bảng "users"
mycursor.execute("CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255))")

# Tạo bảng "profiles"
mycursor.execute("CREATE TABLE profiles (id INT PRIMARY KEY, user_id INT, bio VARCHAR(255))")

# Thêm dữ liệu vào bảng "users"
sql = "INSERT INTO users (id, name) VALUES (%s, %s)"
val = (1, "John Doe")
mycursor.execute(sql, val)

# Thêm dữ liệu vào bảng "profiles"
sql = "INSERT INTO profiles (id, user_id, bio) VALUES (%s, %s, %s)"
val = (1, 1, "I'm a software developer")
mycursor.execute(sql, val)

mydb.commit()
