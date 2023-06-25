import sys

# Thiết lập mã ký tự UTF-8 cho xuất dữ liệu
sys.stdout.reconfigure(encoding='utf-8')

import gspread
import matplotlib.pyplot as plt
import tkinter as tk
gs = gspread.service_account('client.json')
sheet = gs.open_by_key('15GyZF-x3IV_1FXGv66rkQ07J0PjUwOh0OBfML4ZNUpA').sheet1
def update_data():
    # Xóa dữ liệu cũ trên giao diện
    listbox.delete(0, tk.END)
    
    # Đọc dữ liệu từ Google Sheet
    data = sheet.get_all_values()
    
    # Hiển thị dữ liệu trên giao diện
    for row in data:
        listbox.insert(tk.END, ' - '.join(row))
    
    # Lặp lại cập nhật sau một khoảng thời gian (vd: 5 giây)
    window.after(5000, update_data)

# Tạo cửa sổ giao diện
window = tk.Tk()

# Tạo thành phần danh sách để hiển thị dữ liệu
listbox = tk.Listbox(window, width=100, height=800)
listbox.pack()

# Cập nhật dữ liệu lần đầu tiên
update_data()

# Khởi chạy cửa sổ giao diện
window.mainloop()