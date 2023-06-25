def calculate_average(lst):
    if len(lst) == 0:
        return 0  # To handle an empty list case
    total = sum(lst)
    average = total / len(lst)
    return average

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Calculate the average value of the list
average = calculate_average(lst)

# Print the result
print("Average:", average)
