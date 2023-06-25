def format_number_with_commas(number):
    # Convert the number to a string
    number_str = str(number)

    # Initialize variables
    formatted_str = ""
    count = 0

    # Iterate through each character in reverse order
    for char in reversed(number_str):
        # Add the character to the formatted string
        formatted_str = char + formatted_str
        count += 1

        # Add a comma after every three characters (except for the last one)
        if count % 3 == 0 and count != len(number_str):
            formatted_str = ',' + formatted_str

    return formatted_str

# Input an integer from the user
input_number = int(input("Enter an integer: "))

# Format the number with comma separators
formatted_number = format_number_with_commas(input_number)

# Print the formatted number
print("Formatted number: ", formatted_number)
