def count_values_greater_than_previous(lst):
    count = 0  # Initialize the count variable to keep track of the number of values satisfying the condition
    for i in range(1, len(lst)):
        if lst[i] > max(lst[:i]):
            count += 1  # Increment the count if the current value is greater than all the previous values
    return count

# Input a list of integers from the user
lst = [int(x) for x in input("Enter a list of integers: ").split()]

# Count the number of values satisfying the condition
count = count_values_greater_than_previous(lst)

# Print the result
print("Number of values satisfying the condition:", count)
