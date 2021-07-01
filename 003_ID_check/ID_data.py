user_code = input('Please enter your ID: ')
if int(user_code[0]) % 2 == 1:
    print('You are male')
else:
    print('You are female')

if user_code[0] in ('1', '2'):
    birth_year = '18'
if user_code[0] in ('3', '4'):
    birth_year = '19'
if user_code[0] in ('5', '6'):
    birth_year = '20'

if int(user_code[7:10]) > 0 and int(user_code[7:10]) <= 10:
    region = 'Kuressaare haigla'
if int(user_code[7:10]) >= 11 and int(user_code[7:10]) <= 19:
    region = 'Tartu Ülikooli Naistekliinik'
if int(user_code[7:10]) >= 21 and int(user_code[7:10]) <= 150:
    region = 'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)'
if int(user_code[7:10]) >= 151 and int(user_code[7:10]) <= 160:
    region = 'Keila haigla'
if int(user_code[7:10]) >= 161 and int(user_code[7:10]) <= 220:
    region = 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)'
if int(user_code[7:10]) >= 221 and int(user_code[7:10]) <= 270:
    region = 'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)'
if int(user_code[7:10]) >= 271 and int(user_code[7:10]) <= 370:
    region = 'Maarjamõisa kliinikum (Tartu), Jõgeva haigla'
if int(user_code[7:10]) >= 371 and int(user_code[7:10]) <= 420:
    region = 'Narva haigla'
if int(user_code[7:10]) >= 421 and int(user_code[7:10]) <= 470:
    region = 'Pärnu haigla'
if int(user_code[7:10]) >= 471 and int(user_code[7:10]) <= 490:
    region = 'Haapsalu haigla'
if int(user_code[7:10]) >= 491 and int(user_code[7:10]) <= 520:
    region = 'Järvamaa haigla (Paide)'
if int(user_code[7:10]) >= 521 and int(user_code[7:10]) <= 570:
    region = 'Rakvere haigla, Tapa haigla'
if int(user_code[7:10]) >= 571 and int(user_code[7:10]) <= 600:
    region = 'Valga haigla'
if int(user_code[7:10]) >= 601 and int(user_code[7:10]) <= 650:
    region = 'Viljandi haigla'
if int(user_code[7:10]) >= 651 and int(user_code[7:10]) <= 700:
    region = 'Lõuna-Eesti haigla (Võru), Põlva haigla'

print('You were born on ' + (user_code[5]) + (user_code[6]) + '.' + (user_code[3]) + (user_code[4]) + '.' + birth_year + (user_code[1]) + (user_code[2]) + ' at ' + (region))
