def find_first_positive(lst):
    for num in lst:
        if num > 0:
            return num
    return -1

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Find the first positive value in the list
first_positive = find_first_positive(lst)

# Print the result
print(first_positive)
