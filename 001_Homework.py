number = (input('Please enter any number:'))
# проверка на четность/нечетность числа
if (int(number) % 2) == 0:
    print('The number', (number), 'is even')
else:
    print('The number', (number), 'is odd')
# возведение в квадрат
print('Your number', (number), 'raised to the 2nd power is:', float(number) ** 2)
# оличество символов в числе
if len(str(number)) == 1:
    print('There is', len(str(number)), 'digit in your number')
elif len(str(number)) >= 2:
    print('There are', len(str(number)), 'digits in your number')