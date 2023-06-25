def find_string_with_highest_uppercase(L):
    highest_position = -1
    result_string = None

    for string in L:
        for i, char in enumerate(string):
            if char.isupper() and i > highest_position:
                highest_position = i
                result_string = string

    return result_string

# Input a list of strings
L = input("Enter a list of strings: ").split()

# Find the string with the highest position of an uppercase letter
result = find_string_with_highest_uppercase(L)

# Print the result
if result is not None:
    print("String with highest uppercase position:", result)
else:
    print("No uppercase letters found in the list.")
