def say_hello():
    a = "Hello"
    print(a)

# Lỗi: name 'a' is not defined

a = "Hello Guy!"
def say(a):
    a = "Toidicode.com"
    print(a)

say(a)
# KQ: Toidicode.com
print(a)
# KQ: Hello Guy!

a = [5, 10, 15]
def change(a):
    a[0] = 1000
    print(a)

change(a)
# KQ: [1000, 10, 15]
print(a)
# KQ: [1000, 10, 15]

a = "Hello Guy!"
def say():
    global a
    a = "Toidicode.com"
    print(a)

say()
# KQ: Toidicode.com
print(a)
# KQ: Toidicode.com

def get_sum(*num):
    tmp = 0
    # duyet cac tham so
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)

print(result)
# KQ: 15