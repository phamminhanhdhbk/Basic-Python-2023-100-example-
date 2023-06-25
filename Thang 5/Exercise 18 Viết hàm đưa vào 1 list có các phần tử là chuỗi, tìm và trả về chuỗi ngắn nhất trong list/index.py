def calculate_average(L, a):
    if a <= 0:
        return None
    if len(L) < a:
        return None
    sum_a_elements = sum(L[:a])
    average = sum_a_elements / a
    return average

my_list = [2, 4, 6, 8, 10, 12]
num_elements = 4

result = calculate_average(my_list, num_elements)
print("Average of the first", num_elements, "elements:", result)
