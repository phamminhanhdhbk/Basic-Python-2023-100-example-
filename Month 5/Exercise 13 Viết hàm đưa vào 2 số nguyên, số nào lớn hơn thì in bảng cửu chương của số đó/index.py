def print_multiplication_table(a, b):
    # Determine the larger number
    if a > b:
        number = a
    else:
        number = b

    # Print the multiplication table of the larger number
    print("Multiplication Table of", number)
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

# Input two integers from the user
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Print the multiplication table of the larger number
print_multiplication_table(a, b)
