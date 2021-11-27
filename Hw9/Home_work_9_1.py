# 1) Напишите функцию, которая вернет максимальное число из списка чисел.

def get_list_max(i_list):
    # варіант1  max_number = max(i_list)
    # варіант2
    max_number = i_list[0]
    for i in range(1, len(i_list)):
        if max_number < i_list[i]:
            max_number = i_list[i]
    return max_number


list_test = [1, 23, 45, 678, 90, 9]
max_list_test = get_list_max(list_test)
print('List of numbers:', list_test)
print('Max_number is:', max_list_test)
