# Реализуйте  функцию,  параметрами  которой  являются  -  два  числа  и  строка.
# Возвращает она конкатенацию строки с суммой чисел.

def adding_str_num(a, b, inp_str):
    return inp_str + str(a + b)


result = adding_str_num(2, 5, "apples")
print(result)
