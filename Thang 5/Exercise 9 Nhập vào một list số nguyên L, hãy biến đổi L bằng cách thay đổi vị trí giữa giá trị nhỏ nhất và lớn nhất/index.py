def swap_min_max(L):
    if len(L) < 2:
        return L  # Return the list as is if it has less than 2 elements

    min_value = min(L)
    max_value = max(L)
    min_index = L.index(min_value)
    max_index = L.index(max_value)

    # Swap the positions of the minimum and maximum values
    L[min_index], L[max_index] = L[max_index], L[min_index]

    return L

# Input a list of integers from the user
L = [int(x) for x in input("Enter a list of integers: ").split()]

# Swap the minimum and maximum values in the list
transformed_list = swap_min_max(L)

# Print the transformed list
print("Transformed list:", transformed_list)
