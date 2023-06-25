# -*- coding: utf-8 -*-
import mysql.connector
# cài thư viện sau python -m pip install mysql-connector
# Kết nối tới cơ sở dữ liệu
mydb = mysql.connector.connect(
  host="localhost",       # Địa chỉ máy chủ MySQL
  user="root",        # Tên người dùng MySQL
  password="",    # Mật khẩu MySQL
  database="w3stop_specialstar"     # Tên cơ sở dữ liệu
)

# Tạo đối tượng cursor để thực hiện các truy vấn
cursor = mydb.cursor()

# Ví dụ: Thực hiện một truy vấn SELECT
cursor.execute(u"SELECT * FROM analytics")

# Lấy tất cả các kết quả từ truy vấn SELECT
results = cursor.fetchall()

# In ra tất cả các kết quả
for row in results:
    print(row)

# Đóng kết nối
mydb.close()
