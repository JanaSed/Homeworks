import re

colors = '''
HTML / CSS
Color Name
Hex Code
#RRGGBB
Decimal Code
(R,G,B)
coral
#FF7F50
rgb(255,127,80)
tomato
#FF6347
rgb(255,99,71)
orangered
#FF4500
rgb(255,69,0)
gold
#FFD700
rgb(255,215,0)
orange#FFA500rgb(255,165,0)
darkorange
#FF8C00 rgb(255,140,0)
47507220344
77507220344
7750722034
'''
numbers = '''
2*9-6*5 (3+5)-9*4
'''
time = '''
breakfast at 09:00
some not time 37:98
'''

# pattern = re.compile(r'#[A-Z0-9]{6}')
# matches = pattern.finditer(colors)
#
# pattern = re.compile(r'\d[*()-]')
# matches = pattern.finditer(numbers)
#
# pattern = re.compile(r'[0-23][0-59]:[0-23][0-59]')
# matches = pattern.finditer(time)
#
# for match in matches:
#     print(match)

with open('people.txt', 'r', encoding='utf8') as file:
    data = file.read()
# pattern = re.compile(r'[A-Z][\'a-z]+\s[A-Z][\'a-z]+[-]?[A-Z][\'a-z]+')
# matches = pattern.findall(data)
# print(matches)

# Dave Martin
# Jennifer Martin-White  - [\s-]?[A-Z][\'a-z]+


pattern = re.compile(r'[\d{3}]\s[A-Z0-9][a-z]+\s[St\.,]\s[A-Z][a-z]+\s[A-Z]{2}\s[\d{5}]')
matches = pattern.findall(data)
print(matches)
# # # 884 High St., Braavos ME 43597

# pattern = re.compile(r'[A-Za-z]*')
# matches = pattern.finditer(colors)
# for match in matches:
#     print(match)

# pattern = re.compile(r'[3-6]\d{10}')
# matches = pattern.finditer(colors)
# for match in matches:
#     print(match)