import random
from random import randint

for x in range(5):
    a = randint(1, 48)
    print(a, end=' ')
print()
for y in range(2):
    b = randint(1, 5)
    print(b, end=' ')

print()

print(random.sample(range(50), 5))
print(random.sample(range(1, 5), 2))
