option = [12,5,1996]
myList = ['Vu Thanh Tai', option]
print(myList)
# ['Vu Thanh Tai', [12, 5, 1996]]

subList = myList[1] # [12, 5, 1996]
subList[0] # 12

# hoặc có thể viết ngắn gọn như sau
myList[1][0] # 12

print("lay bien trong nest list")
print(myList[1][0])