def rearrange_list(L):
    evens = []  # List to store even numbers
    odds = []  # List to store odd numbers
    zeros = []  # List to store zeros

    for num in L:
        if num == 0:
            zeros.append(num)
        elif num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    return evens + zeros + odds

# Input a list of integers from the user
L = [int(x) for x in input("Enter a list of integers: ").split()]

# Rearrange the list
rearranged_list = rearrange_list(L)

# Print the rearranged list
print("Rearranged list:", rearranged_list)
