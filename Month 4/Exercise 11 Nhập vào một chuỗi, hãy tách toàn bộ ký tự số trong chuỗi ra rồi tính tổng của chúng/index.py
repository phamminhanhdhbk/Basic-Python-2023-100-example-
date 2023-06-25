def extract_and_calculate_sum(input_string):
    digits = []
    total_sum = 0

    for char in input_string:
        if char.isdigit():
            digits.append(int(char))

    if digits:
        total_sum = sum(digits)

    return total_sum

# Nhập chuỗi từ người dùng
input_string = input("input: ")

# Tách toàn bộ ký tự số trong chuỗi và tính tổng
result = extract_and_calculate_sum(input_string)

print("Result:", result)
