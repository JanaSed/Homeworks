test_list1 = [1, 2, 3, 4, 4, 4, 7, 9, 9, 9]
# most_freq = some_list.count(9)
#
# print('The most frequent number is:', ())

# var 1:
max_count = 0
# через цикл пропускаем каждое число +1
new_list = []
for num in test_list1:
    if test_list1.count(num) > max_count:
        max_count = test_list1.count(num)
for num in test_list1:
    if test_list1.count(num) == max_count:
        new_list.append(num)
# print(new_list)
new_list = list(set(new_list))

print(new_list)

# var 2:
empty_dict = {}


