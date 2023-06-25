def find_max_value(lst):
    # Initialize the maximum value as the first element of the list
    max_value = lst[0]

    # Iterate through the remaining elements of the list
    for num in lst[1:]:
        # Update the maximum value if a larger number is found
        if num > max_value:
            max_value = num

    return max_value

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Find the maximum value in the list
max_value = find_max_value(lst)

# Print the maximum value
print("Maximum value:", max_value)
