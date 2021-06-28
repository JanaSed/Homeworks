# 0-100
# Если число делится на 3 без остатка - написать Fizz
# Если число делится на 5 без остатка - написать Buzz
# Если число делится на 3 и на 5 без остатка - написать FizzBuzz

for num in range(0, 100):
    if num % 3 == 0:
        print(num, 'Fizz')
    if num % 5 == 0:
        print(num, 'Buzz')
    if num % 3 == 0 and num % 5 == 0:
        print(num, 'FizzBuzz')
