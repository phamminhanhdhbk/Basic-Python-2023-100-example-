import sys

# Thiết lập mã ký tự UTF-8 cho xuất dữ liệu
sys.stdout.reconfigure(encoding='utf-8')

import gspread
import matplotlib.pyplot as plt
import tkinter as tk
gs = gspread.service_account('client.json')
sheet = gs.open_by_key('15GyZF-x3IV_1FXGv66rkQ07J0PjUwOh0OBfML4ZNUpA').sheet1
# Đọc dữ liệu từ Google Sheet
data = sheet.get_all_values()

# Tạo cửa sổ giao diện
window = tk.Tk()

# Tạo thành phần danh sách để hiển thị dữ liệu
listbox = tk.Listbox(window, width=50, height=10)

# Hiển thị dữ liệu trên thành phần danh sách
for row in data:
    listbox.insert(tk.END, ' - '.join(row))

listbox.pack()

# Khởi chạy cửa sổ giao diện
window.mainloop()
