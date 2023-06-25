def find_smallest_integer(L):
    integers = [x for x in L if isinstance(x, int)]
    if not integers:
        return None
    smallest_integer = min(integers)
    return smallest_integer

# Input a list containing strings and integers
L = input("Enter a list of strings and integers: ").split()

# Find the longest string in the list
longest_string = max(L, key=len) if any(isinstance(x, str) for x in L) else None

# Find the smallest integer in the list
smallest_integer = find_smallest_integer(L)

# Print the results
print("Longest string:", longest_string)
print("Smallest integer:", smallest_integer)
