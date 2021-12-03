#  Существуют такие последовательности чисел:
# 0,2,4,6,8,10,12 -- n + 2
# 1,4,7,10,13     -- n + 3
# 1,2,4,8,16,32   --- 2^index
# 1,3,9,27        --- 3^index
# 1,4,9,16,25     --- 1^2 2^2 3^2 4^2 5^2
# 1,8,27,64,125   --- 1^3, 2^3 3^3, 4^3, 5^3
# Реализуйте программу, которая выведет следующий член этой последовательности
# (либо  подобной  им)  на  экран.  Последовательность  пользователь  вводит  с
# клавиатуры в виде строки. Например, пользователь вводит строку 0,5,10,15,20,25 и
# ответом программы должно быть число 30.
import math

list_1 = [0, 2, 4, 6, 8, 10, 12]
list_2 = [1, 2, 4, 8, 16, 32]
list_3 = [1, 3, 9, 27]
list_4 = [1, 4, 9, 16, 25]
list_5 = [1, 8, 27, 64, 125]


def check_list(input_list):
    set_func = set()
    lst_len = len(input_list) - 1
    answer_func = {}
    for i in range(1, len(input_list)):
        if input_list[i] - input_list[i - 1] == 2:
            set_func.add('add2')
        elif input_list[i] - input_list[i - 1] == 3:
            set_func.add('add3')
        elif pow(2, i) == input_list[i]:
            set_func.add('pow2i')
        elif pow(3, i) == input_list[i]:
            set_func.add('pow3i')
        elif math.sqrt(input_list[i]) - math.sqrt(input_list[i - 1]) == 1:
            set_func.add('powi2')
        elif (input_list[i]) ** 1 / 3 - (input_list[i - 1]) ** 1 / 3 == 1:
            set_func.add('powi3')
        else:
            set_func.add('unknown')
    if len(set_func) == 1:
        func_type = str(set_func).replace("'", "").replace("}", "").replace("{", "")
    else:
        func_type = 'unknown_operation'

    return func_type


def get_last_element(input_list):
    last_elem = input_list[len(input_list) - 1]
    return last_elem


func = check_list(list_1)
print(func)
