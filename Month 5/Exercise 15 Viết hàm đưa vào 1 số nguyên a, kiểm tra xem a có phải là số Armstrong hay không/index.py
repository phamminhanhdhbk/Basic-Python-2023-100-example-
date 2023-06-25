def is_armstrong(a):
    # Convert the integer 'a' to a string
    str_a = str(a)

    # Count the number of digits in 'a'
    num_digits = len(str_a)

    # Initialize the total variable
    total = 0

    # Iterate over each digit in 'str_a'
    for digit in str_a:
        # Convert the digit back to integer and compute its power
        total += int(digit) ** num_digits

    # Check if the total is equal to 'a'
    if total == a:
        return True
    else:
        return False

# Input an integer from the user
num = int(input("Enter an integer: "))

# Check if the number is Armstrong
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
