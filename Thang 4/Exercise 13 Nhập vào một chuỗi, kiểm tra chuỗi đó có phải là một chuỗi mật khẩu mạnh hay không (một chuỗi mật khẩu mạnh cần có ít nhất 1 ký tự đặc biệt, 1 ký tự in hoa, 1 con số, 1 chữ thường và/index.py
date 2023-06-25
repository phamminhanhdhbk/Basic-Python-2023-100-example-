import re

def is_strong_password(input_string):
    # Kiểm tra độ dài của chuỗi
    if len(input_string) <= 6:
        return False

    # Kiểm tra ký tự đặc biệt
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', input_string):
        return False

    # Kiểm tra ký tự in hoa
    if not re.search(r'[A-Z]', input_string):
        return False

    # Kiểm tra ký tự con số
    if not re.search(r'\d', input_string):
        return False

    # Kiểm tra ký tự chữ thường
    if not re.search(r'[a-z]', input_string):
        return False

    return True

# Nhập chuỗi từ người dùng
input_string = input("Input: ")

# Kiểm tra xem chuỗi có là mật khẩu mạnh hay không
if is_strong_password(input_string):
    print("String Strong.")
else:
    print("String Not Strong.")
