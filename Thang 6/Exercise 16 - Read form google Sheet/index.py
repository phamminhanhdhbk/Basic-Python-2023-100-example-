import gspread
gs = gspread.service_account('client.json')
sht = gs.open_by_key('15GyZF-x3IV_1FXGv66rkQ07J0PjUwOh0OBfML4ZNUpA').sheet1
# print(sht.title)
data = sht.get_all_values()
# In ra dữ liệu
for row in data:
    print(row)