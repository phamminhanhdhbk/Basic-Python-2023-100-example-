def find_nth_largest(L, a):
    if a <= 0 or a > len(L):
        return None
    
    sorted_list = sorted(L, reverse=True)
    return sorted_list[a - 1]

my_list = [5, 2, 9, 1, 7, 4, 8]
n = 3

result = find_nth_largest(my_list, n)
print("The", n, "-th largest value is:", result)
