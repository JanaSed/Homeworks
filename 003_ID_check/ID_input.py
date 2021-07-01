while True:
    try:
        user_code = input('Please enter your ID: ')
        user_code = str(int(user_code))
        print(user_code)
        if len(user_code) != 11:
            raise UserWarning

    except UserWarning:
        print('Entered ID is incorrect, doesn\'t consist 11 numbers.')
        continue
    except ValueError:
        print('Entered ID is not numeric')
        continue
    else:
        print(input('Please choose an option:\n'
                              '1. ID data\n'
                              '2. Validate\n'
                              '3. Exit\n'
                              '--> '))
