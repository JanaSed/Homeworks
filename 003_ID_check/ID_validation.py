check_1 = [1,2,3,4,5,6,7,8,9,1]
check_2 = [3,4,5,6,7,8,9,1,2,3]
# print(type(check_1))

user_code = input('Please enter your ID: ')
# print(type(user_code))
x = 0
for check in range(0, 10):
    x += check_1[check] * int(user_code[check])
y = x % 11
if y >= 10:
    for check in range(0, 10):
        x += check_2[check] * int(user_code[check])
    y = x % 11
if y == int(user_code[10]):
    print('ID is valid')
else:
    print('ID is invalid')