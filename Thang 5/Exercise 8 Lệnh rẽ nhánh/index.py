a = 100
if (a == 100):
    print('Dung')
# Ket qua: Dung

a = 7
if (a >= 0 and a <= 10):
    if (a >= 4):
        print('Qua mon')
    else:
        print('Hoc lai')
else:
    print('Diem khong hop le')
# Ket qua: Qua mon

a = 9
if (a >= 4 and a <= 10):
    print('Qua mon')
elif (a >= 0 and a <4):
    print('Hoc lai')
else:
    print('Diem khong hop le')
# Ket qua: Qua mon

a = 'hai'
dic = {
    'mot': 1,
    'hai': 2,
    'ba': 3,
}
print(dic.get(a,'khong ro'))
# Ket Qua: 2