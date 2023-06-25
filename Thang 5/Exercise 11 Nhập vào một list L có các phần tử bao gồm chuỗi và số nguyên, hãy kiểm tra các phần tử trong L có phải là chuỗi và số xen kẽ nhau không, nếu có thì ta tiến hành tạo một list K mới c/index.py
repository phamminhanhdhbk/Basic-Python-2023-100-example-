# Nhập vào một list L có các phần tử bao gồm chuỗi và số nguyên, hãy kiểm tra các phần tử trong L có phải là chuỗi và số xen kẽ nhau không, nếu có thì ta tiến hành tạo một list K mới có các phần tử như sau
# K[i2] = L[i]L[i+1] (với i chẵn)
def create_new_list(L):
    if len(L) % 2 != 0:
        return None

    K = []
    for i in range(0, len(L), 2):
        if isinstance(L[i], str) and isinstance(L[i + 1], int):
            K.append(L[i] * L[i + 1])
        else:
            return None

    return K

# Input a list containing strings and integers
L = input("Enter a list of strings and integers: ").split()

# Create a new list based on the given condition
new_list = create_new_list(L)

# Print the new list if it exists, otherwise print None
if new_list is not None:
    print("New list:", new_list)
else:
    print("No valid new list can be created.")
