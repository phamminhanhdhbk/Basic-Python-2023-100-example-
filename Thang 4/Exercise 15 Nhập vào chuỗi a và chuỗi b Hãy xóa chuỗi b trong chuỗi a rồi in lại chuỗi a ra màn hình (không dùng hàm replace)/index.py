def remove_substring(string_a, string_b):
    # Find the length of string b
    len_b = len(string_b)
  
    # Initialize an empty result string
    result = ""

    # Iterate through string a
    i = 0
    while i < len(string_a):
        # Check if substring b is found starting at the current position
        if string_a[i:i+len_b] == string_b:
            # Skip the substring b
            i += len_b
        else:
            # Append the character to the result string
            result += string_a[i]
            i += 1

    return result

# Input strings a and b from the user
string_a = input("Enter string a: ")
string_b = input("Enter string b: ")

# Remove string b from string a
updated_string_a = remove_substring(string_a, string_b)

# Print the updated string a
print("Updated string a:", updated_string_a)
