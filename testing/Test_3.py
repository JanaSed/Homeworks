a, b, c = input("Please enter sides a, b, c. Split with space. ").split()
a, b, c = float(a), float(b), float(c)
if c * c == (a * a) + (b * b):
    print('Triangle is right-angled')
else:
    print('Triangle is not right-angled')
