# Người ta định nghĩa một list số nguyên được gọi là “dạng sóng” khi tất cả các phần tử đều lớn hơn hoặc nhỏ hơn hai phần tử xung quanh nó.
# Nhập vào một list số nguyên L và kiểm tra xem L có phải là list “dạng sóng” hay không, nếu có thì ta in ra True, không có thì ta in False
def check_wave_list(lst):
    if len(lst) < 3:
        return False  # A wave list requires at least 3 elements
    for i in range(1, len(lst) - 1):
        if (lst[i] <= lst[i-1] and lst[i] <= lst[i+1]) or (lst[i] >= lst[i-1] and lst[i] >= lst[i+1]):
            continue
        else:
            return False
    return True

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Check if the list is a wave list
is_wave_list = check_wave_list(lst)

# Print the result
print(is_wave_list)
