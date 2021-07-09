import datetime

today = datetime.date.today()
user_input = input('Please enter your birth date DD.MM.YYYY: ')
# user_date = input(int('Please enter your birth date DD.MM.YYYY: ').split('.'))
user_date = datetime.datetime.strptime(user_input, '%d.%m.%Y')
# аааа, не получается эта .timedelta :(
last_bd = (today.day - datetime.timedelta(days=365).days)
next_bd = (datetime.timedelta(days=365).days - user_date.day)

print('Your last birthday was', abs(last_bd), 'days ago.')
print('Your next birthday is in', abs(next_bd), 'days.')
if last_bd < 365:
    print('You are', (today.year - user_date.year) - 1, 'years old.')
else:
    print('You are', today.year - user_date.year, 'years old.')



