person = {
    'name': 'Pham Minh Anh',
    'age': 22,
    'male': True,
    'status': 'alone'        
    }
print('truoc khi xoa status')
print(person)
del person['status']
print(person)
#{'name': 'Vu Thanh Tài', 'age': 22, 'male': True}