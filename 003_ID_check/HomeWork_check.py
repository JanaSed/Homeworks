user_code = input('Please enter ID code: ')
user_choice = input('Please choose\n1. Get data\n2. Validate\n3. Exit\n-->  ')
if user_choice == '1':
# check id owners gender
    if int(user_code[0]) % 2 == 0:
        gender = 'Female'
    else:
        gender = 'Male'

# check id owners birth century
    if user_code[0] =='1' or user_code[0] == '2':
        birth_cent = '18'
    elif user_code[0] =='3' or user_code[0] == '4':
        birth_cent = '19'
    elif user_code[0] =='5' or user_code[0] == '6':
        birth_cent = '20'

    by = user_code[1:3]
    bm = user_code[3:5]
    bd = user_code[5:7]
    birth_region = user_code[7:10]
    chk_number = user_code[10]

    if int(user_code[7:10]) > 0 and int(user_code[7:10]) <= 10:
        region = 'Kuressaare haigla'
    elif int(user_code[7:10]) >= 11 and int(user_code[7:10]) <= 19:
        region = 'Tartu Ülikooli Naistekliinik'
    elif int(user_code[7:10]) >= 21 and int(user_code[7:10]) <= 150:
        region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
    elif int(user_code[7:10]) >= 151 and int(user_code[7:10]) <= 160:
        region = 'Keila haigla'
    elif int(user_code[7:10]) >= 161 and int(user_code[7:10]) <= 220:
        region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
    elif int(user_code[7:10]) >= 221 and int(user_code[7:10]) <= 270:
        region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
    elif int(user_code[7:10]) >= 271 and int(user_code[7:10]) <= 370:
        region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
    elif int(user_code[7:10]) >= 371 and int(user_code[7:10]) <= 420:
        region = 'Narva haigla'
    elif int(user_code[7:10]) >= 421 and int(user_code[7:10]) <= 470:
        region = 'Pärnu haigla'
    elif int(user_code[7:10]) >= 471 and int(user_code[7:10]) <= 490:
        region = 'Haapsalu haigla'
    elif int(user_code[7:10]) >= 491 and int(user_code[7:10]) <= 520:
        region = 'Järvamaa haigla (Paide)'
    elif int(user_code[7:10]) >= 521 and int(user_code[7:10]) <= 570:
        region = 'Rakvere haigla, Tapa haigla'
    elif int(user_code[7:10]) >= 571 and int(user_code[7:10]) <= 600:
        region = 'Valga haigla'
    elif int(user_code[7:10]) >= 601 and int(user_code[7:10]) <= 650:
        region = 'Viljandi haigla'
    elif int(user_code[7:10]) >= 651 and int(user_code[7:10]) <= 700:
        region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'
    else:
        region = 'Unknown'

#  print result
    print(f'Your ID code is {user_code}')
    print(f'You are {gender}')
    print(f'Your date of birth is {bd}, {bm}, {birth_cent}{by}')
    print(f'Your were born in {region}')
    print(f'Your check number is {chk_number}')


elif user_choice == '2':
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    chk_result = 0
    cnt_index = 0
    for num in chk1:
        chk_result += int(user_code[cnt_index]) * chk1[cnt_index]
        cnt_index += 1
    if chk_result % 11 == 10 or chk_result % 11 == 0:
        # обнуляем, так как уже им присвоилис переменные после первого цикла
        chk_result = 0
        cnt_index = 0
        for num in chk2:
            chk_result += int(user_code[cnt_index]) * chk2[cnt_index]
            cnt_index += 1
        if chk_result % 11 == int(user_code[10]):
            print('Code is valid. Used second range')
    elif chk_result % 11 == int(user_code[10]):
        print('Code is valid. Used first range')
    else:
        print('Code is not valid. Used first range')

elif user_choice == '3':
    pass
else:
    print()