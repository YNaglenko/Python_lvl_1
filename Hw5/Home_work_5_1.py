# 1 )Дан список [0,5,2,4,7,1,3,19]. Написать программу для подсчета нечетных цифр в нем.
number_list = [0, 5, 2, 4, 7, 1, 3, 19]
sum_odd = 0
for i in number_list:
    if i % 2 > 0:
        sum_odd = sum_odd + i
print('List of numbers:', number_list)
print('Total sum of the odd numbers:', sum_odd)
