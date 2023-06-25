import sys

# Thiết lập mã ký tự UTF-8 cho xuất dữ liệu
sys.stdout.reconfigure(encoding='utf-8')

import gspread
gs = gspread.service_account('client.json')
sheet = gs.open_by_key('15GyZF-x3IV_1FXGv66rkQ07J0PjUwOh0OBfML4ZNUpA').sheet1
# print(sht.title)
data = sheet.get_all_values()
# Thêm các hàng mới vào bảng tính
new_rows = [
    ['1', '2', '3'],
    ['3', '4', '5'],
]


for row in new_rows:
    sheet.append_row(row)

# In ra dữ liệu sau khi thêm hàng mới
data = sheet.get_all_values()
for row in data:
    print(row)