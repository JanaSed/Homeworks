# # проверка на четность/нечетность числа
# number = int(input('Please enter a number:'))
# if (number) % 2 == 0:
#     print('The number', (number), 'is even')
# else:
#     print('The number', (number), 'is odd')
# # возведение в квадрат
# print('Your number', (number), 'raised to the 2nd power is:', (number) ** 2)
# # количество символов в числе
# if len(str(number)) == 1:
#     print('There is', len(str(number)), 'digit in your number')
# elif len(str(number)) >= 2:
#     print('There are', len(str(number)), 'digits in your number')


user_number = input('Please enter some number: ')
user_number_len = len(user_number)
if int(user_number) % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')

print(int(user_number) ** 2)
if user_number_len == 1:
    print('There is' + str(user_number_len) + ' digit in number' + user_number)
elif user_number_len > 1:
    print('There are' + str(user_number_len) + ' digits in number' + user_number)