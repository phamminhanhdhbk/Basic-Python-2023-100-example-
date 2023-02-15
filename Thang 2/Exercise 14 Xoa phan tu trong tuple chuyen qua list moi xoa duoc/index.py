my_tuple = (1, 2, 3, 4, 5)
print("Before deletion:", my_tuple)

# Chuyển đổi tuple thành list và xóa phần tử đầu tiên
my_list = list(my_tuple)
del my_list[0]

# Chuyển đổi list thành tuple
my_tuple = tuple(my_list)

print("After deletion:", my_tuple)
