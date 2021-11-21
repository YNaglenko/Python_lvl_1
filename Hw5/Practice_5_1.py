import random

my_list = []
count_odd = 0
sum_odd = 0

for i in range(20):
    my_list.append(random.randint(1, 10))
    if my_list[i] % 2 != 0:
        count_odd = count_odd + 1
        sum_odd = sum_odd + my_list[i]
print(my_list)
print(sum_odd, sum_odd // count_odd)

