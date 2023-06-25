def count_character_types(input_string):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1

    return uppercase_count, lowercase_count, digit_count

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi: ")

# Đếm số ký tự in hoa, in thường và số ký tự số trong chuỗi
uppercase, lowercase, digits = count_character_types(input_string)

print("Số ký tự in hoa trong chuỗi là:", uppercase)
print("Số ký tự in thường trong chuỗi là:", lowercase)
print("Số ký tự số trong chuỗi là:", digits)
