# Написать функцию с параметр = список
# которая выведет сумму нечетных чисел

def sum_odd_num(i_list):
    sum_odd = 0
    for element in i_list:
        if element % 2 > 0:
            sum_odd = sum_odd + element
    return sum_odd


my_list = [1, 2, 4, 6, 3, 7]
summa = sum_odd_num(my_list)
print(summa)
