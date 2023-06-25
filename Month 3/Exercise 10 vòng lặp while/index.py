i = 1
sum = 0
while i <= 10:
  sum += i
  i += 1
print("Tong so tu 1 den 10 la", sum)


i = 2
while i <= 10:
  print(i)
  i += 2

string = "Hello, world!"
length = 0
while string:
  length += 1
  string = string[1:]
print("Do Dai cua chuoi Hello, world la:", length)


import random
number = random.randint(1, 100)
guess = 0
while guess != number:
  guess = int(input("Doan so tu 1 den 100: "))
  if guess > number:
    print("So ban doan qua luon")
  elif guess < number:
    print("So ban doan qua nho")
print("Chuc mung ban da doan dung so")
