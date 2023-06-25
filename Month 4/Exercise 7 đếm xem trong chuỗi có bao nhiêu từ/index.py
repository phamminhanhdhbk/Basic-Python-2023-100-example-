import re

def count_words(input_string):
    # Loại bỏ các ký tự không phải chữ và khoảng trắng
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string)
    
    # Tách chuỗi thành các từ
    words = cleaned_string.split()
    
    # Đếm số từ
    word_count = len(words)
    
    return word_count

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi: ")

# Đếm số từ trong chuỗi
result = count_words(input_string)

print("Số từ trong chuỗi là:", result)
