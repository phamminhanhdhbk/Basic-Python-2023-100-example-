def find_position(lst):
    for i in range(1, len(lst) - 1):
        if lst[i] == lst[i-1] * lst[i+1]:
            return i
    return -1

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Find a position that satisfies the conditions
position = find_position(lst)

# Print the result
print("Position:", position)

# Người ta định nghĩa một list số nguyên là list chẵn lẻ, nếu như tổng 2 phần tử bất kỳ bên trong list đều là số lẻ Nhập vào một list số nguyên L và kiểm tra xem L có phải là list chẵn lẻ hay không