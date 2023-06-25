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

# Tạo bảng "posts"
mycursor.execute("CREATE TABLE posts (id INT PRIMARY KEY, user_id INT, title VARCHAR(255), content TEXT)")

# Thêm dữ liệu vào bảng "users"
sql = "INSERT INTO users (id, name) VALUES (%s, %s)"
val = (1, "John Doe")
mycursor.execute(sql, val)

# Thêm dữ liệu vào bảng "posts"
sql = "INSERT INTO posts (id, user_id, title, content) VALUES (%s, %s, %s, %s)"
val = (1, 1, "Hello World", "This is my first post.")
mycursor.execute(sql, val)

mydb.commit()
