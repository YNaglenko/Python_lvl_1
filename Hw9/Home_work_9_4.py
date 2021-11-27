# Напишите функцию, которая реализует линейный поиск элемента в списке целых
# чисел.  Если  такой  элемент  в  списке  есть,  то  верните  его  индекс,  если  нет,  то
# верните число «-1».

def search_index(i_list, n):
    for i in range(len(i_list)):
        if i_list[i] == n:
            f_index = i
            break
        else:
            f_index = - 1
    return f_index


lst = [45, 5, 18, 121, 134, 2, 44]
print('Index is:', search_index(lst, 121))
