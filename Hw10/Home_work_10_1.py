# 1)  Напишите  функцию,  которая  вернет  сумму  всех  нечетных  элементов  списка.
# Например, для списка вида [2,1,4,6,3]  ваша программа должна вернуть 4.

def list_sum_odd(i_list):
    total = 0
    for element in i_list:
        if element % 2 != 0:
            total = total + element
    return total


test_list = [1, 3, -3, 50, 17, -9, -33]
total_odd = list_sum_odd(test_list)
print('Test_List:', test_list, 'and total sum of the odd numbers:', total_odd)
