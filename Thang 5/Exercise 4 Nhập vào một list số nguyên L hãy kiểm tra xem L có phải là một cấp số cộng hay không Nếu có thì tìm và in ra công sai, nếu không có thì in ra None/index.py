def check_arithmetic_progression(lst):
    if len(lst) < 2:
        return None  # An AP requires at least 2 elements
    difference = lst[1] - lst[0]  # Calculate the difference between the first two elements
    for i in range(2, len(lst)):
        if lst[i] - lst[i-1] != difference:
            return None
    return difference

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Check if the list forms an arithmetic progression
common_difference = check_arithmetic_progression(lst)

# Print the result
print("Common difference:", common_difference)
