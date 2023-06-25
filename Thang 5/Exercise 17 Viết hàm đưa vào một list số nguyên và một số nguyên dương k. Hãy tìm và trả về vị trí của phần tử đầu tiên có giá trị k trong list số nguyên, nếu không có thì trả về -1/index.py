def find_first_occurrence(numbers, k):
    for i in range(len(numbers)):
        if numbers[i] == k:
            return i
    return -1

my_list = [3, 5, 2, 8, 5, 4]
target = 5

index = find_first_occurrence(my_list, target)
print("Index of the first occurrence:", index)
