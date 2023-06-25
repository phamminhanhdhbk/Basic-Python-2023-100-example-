def find_prime_numbers(L, a):
    if a <= 0:
        return []
    
    prime_numbers = []
    count = 0
    
    for num in L:
        if is_prime(num):
            prime_numbers.append(num)
            count += 1
            if count == a:
                break
    
    return prime_numbers


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
num_elements = 3

result = find_prime_numbers(my_list, num_elements)
print("List of prime numbers:", result)

