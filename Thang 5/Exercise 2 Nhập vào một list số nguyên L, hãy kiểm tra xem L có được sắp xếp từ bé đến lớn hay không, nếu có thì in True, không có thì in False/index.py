def check_sorted(lst):
    return lst == sorted(lst)

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Check if the list is sorted
is_sorted = check_sorted(lst)

# Print the result
print(is_sorted)
