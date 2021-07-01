try:
    user_code = input('Please enter your ID: ')
    if len(user_code) != 11:
        raise UserWarning
    user_code = int(user_code)
except UserWarning:
    print('Entered ID is incorrect, doesn\'t consist 11 numbers.')
except ValueError:
    print('Entered ID is not numeric')
else:
    print(input('Please choose an option:\n'
                              '1. ID data\n'
                              '2. Validate\n'
                              '3. Exit\n'
                              '--> '))
