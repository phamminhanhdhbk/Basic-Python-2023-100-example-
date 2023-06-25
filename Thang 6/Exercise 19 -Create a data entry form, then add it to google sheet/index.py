import sys

# Thiết lập mã ký tự UTF-8 cho xuất dữ liệu
sys.stdout.reconfigure(encoding='utf-8')

import gspread
import matplotlib.pyplot as plt
import tkinter as tk
gs = gspread.service_account('client.json')
sheet = gs.open_by_key('15GyZF-x3IV_1FXGv66rkQ07J0PjUwOh0OBfML4ZNUpA').sheet1
def add_data_to_sheet():
    name = entry_name.get()
    age = entry_age.get()
    
    # Thêm dữ liệu vào Google Sheet
    sheet.append_row([name, age])
    
    # Xóa nội dung đã nhập trong các ô
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

# Tạo cửa sổ giao diện
window = tk.Tk()

# Đặt kích thước của cửa sổ giao diện
window.geometry("400x200")  # Kích thước là 400 (chiều rộng) x 200 (chiều cao)

# Tạo các thành phần giao diện
label_name = tk.Label(window, text="Tên:")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_age = tk.Label(window, text="Tuổi:")
label_age.pack()
entry_age = tk.Entry(window)
entry_age.pack()

button_submit = tk.Button(window, text="Submit", command=add_data_to_sheet)
button_submit.pack()

# Khởi chạy cửa sổ giao diện
window.mainloop()
