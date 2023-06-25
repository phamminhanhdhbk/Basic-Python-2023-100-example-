def find_max_position(lst):
    # Check if the list is empty
    if len(lst) == 0:
        return None

    # Initialize variables
    max_value = lst[0]  # Assume the first element is the maximum
    max_position = 0    # Initialize the position to 0

    # Iterate over the list starting from the second element
    for i in range(1, len(lst)):
        # Check if the current element is greater than the maximum value
        if lst[i] > max_value:
            max_value = lst[i]       # Update the maximum value
            max_position = i         # Update the position

    return max_position

# Test the function
numbers = [5, 2, 9, 1, 7, 3]
max_pos = find_max_position(numbers)
print("Position of the maximum value:", max_pos)
