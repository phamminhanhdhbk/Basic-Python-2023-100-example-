import sys

# Thiết lập mã ký tự UTF-8 cho xuất dữ liệu
sys.stdout.reconfigure(encoding='utf-8')

import gspread
import matplotlib.pyplot as plt
gs = gspread.service_account('client.json')
sheet = gs.open_by_key('15GyZF-x3IV_1FXGv66rkQ07J0PjUwOh0OBfML4ZNUpA').sheet1
# print(sht.title)
# Đọc dữ liệu từ cột A và B
data = sheet.get('A:B')
# Tách dữ liệu cột A và B thành các danh sách riêng biệt
column_a = [row[0] for row in data]
column_b = [row[1] for row in data]
# Thiết lập dữ liệu cho biểu đồ cột
plt.bar(column_a, column_b)

# Đặt tên cho trục x và trục y
plt.xlabel('Dữ liệu cột A')
plt.ylabel('Dữ liệu cột B')

# Hiển thị biểu đồ
plt.show()
