def find_smallest_number(lst, start, end):
    # Initialize the smallest number as the first number in the specified range
    smallest_number = lst[start]

    # Iterate through the specified range and update the smallest number if a smaller number is found
    for num in lst[start+1:end+1]:
        if num < smallest_number:
            smallest_number = num

    return smallest_number

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Input positive integers a and b
a = int(input("Enter a positive integer a: "))
b = int(input("Enter a positive integer b: "))

# Find the smallest number in the list from position a to position b
smallest_number = find_smallest_number(lst, a, b)

# Print the smallest number
print("Smallest number:", smallest_number)
