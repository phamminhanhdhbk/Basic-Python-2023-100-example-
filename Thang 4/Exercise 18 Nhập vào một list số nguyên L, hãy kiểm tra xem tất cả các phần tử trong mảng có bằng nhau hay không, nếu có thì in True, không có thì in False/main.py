def check_all_elements_equal(lst):
    # Check if all elements in the list are equal to the first element
    return all(x == lst[0] for x in lst)

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Check if all elements in the list are equal
are_all_elements_equal = check_all_elements_equal(lst)

# Print the result
print(are_all_elements_equal)
