# 2)Напишите программу, которая сгенерирует два списка. Один с числами кратными
# 3, другой с числами кратными 5. С помощью множеств создайте список с числами,
# которые есть в обоих множествах.

list_one = []
list_two = []
list_limit = 50
for i in range(1, list_limit):
    if i % 3 == 0:
        list_one.append(i)
    if i % 5 == 0:
        list_two.append(i)
set_one = set(list_one)
set_two = set(list_two)
list_common_digits = list(set_one.intersection(set_two))

print("First list:", list_one, "\n Second list:", list_two, "\n Common digits:", list_common_digits)
