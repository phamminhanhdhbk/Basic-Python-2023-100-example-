def find_largest_negative(lst):
    largest_negative = float('-inf')
    for num in lst:
        if num < 0 and num > largest_negative:
            largest_negative = num
    if largest_negative == float('-inf'):
        return 0
    return largest_negative

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Find the largest negative value in the list
largest_negative = find_largest_negative(lst)

# Print the result
print(largest_negative)
