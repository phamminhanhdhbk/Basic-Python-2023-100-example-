def print_first_word(input_string):
    # Tách chuỗi thành các từ
    words = input_string.split()
    
    if len(words) > 0:
        first_word = words[0]
        print("Từ đầu tiên trong chuỗi là:", first_word)
    else:
        print("Chuỗi không có từ.")

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi: ")

# In từ đầu tiên trong chuỗi
print_first_word(input_string)
