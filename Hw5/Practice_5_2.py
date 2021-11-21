import random
list_num = []

for i in range(20):
    list_num.append(random.randint(1, 10))
max_number = list_num[0]
max_count = list_num.count(max_number)

for element in list_num:
    if max_count < list_num.count(element):
        max_count = list_num.count(element)
        max_number = element
print("Most frequency element is", max_number, 'with result of', max_count)
print(list_num)

