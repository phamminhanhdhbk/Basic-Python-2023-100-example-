def calculate_sum(input_string):
    # Tách chuỗi thành các số nguyên
    numbers = input_string.split(',')
    
    if len(numbers) == 3:
        try:
            # Chuyển đổi các số từ kiểu chuỗi sang kiểu số nguyên
            number1 = int(numbers[0])
            number2 = int(numbers[1])
            number3 = int(numbers[2])
            
            # Tính tổng ba số nguyên
            total_sum = number1 + number2 + number3
            return total_sum
        except ValueError:
            return "Chuỗi không hợp lệ. Vui lòng nhập đúng định dạng 3 số nguyên, cách nhau bằng dấu phẩy."
    else:
        return "Chuỗi không hợp lệ. Vui lòng nhập đúng định dạng 3 số nguyên, cách nhau bằng dấu phẩy."

# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi (3 số nguyên, cách nhau bằng dấu phẩy): ")

# Tính tổng ba số nguyên trong chuỗi
result = calculate_sum(input_string)

print("Tổng ba số nguyên là:", result)
