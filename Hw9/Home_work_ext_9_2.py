# Число-палиндром  с  обеих  сторон  (справа  налево  и  слева  направо)  читается
# одинаково.  Самое  большое  число-палиндром,  полученное  умножением  двух
# двузначных чисел: 9009 = 91 Ч 99. Найдите самый большой палиндром, полученный
# умножением  двух  трехзначных  чисел.  Выведите  значение  этого  палиндрома  и  то,
# произведением каких чисел он является.
max_multi = 0
for i in range(100, 999):
    for j in range(999, 100, -1):
        if i == j:
            break
        else:
            multiply = i * j
            str_number = str(multiply)
            part_len = len(str_number) // 2
            if str_number[:part_len] == str_number[:part_len:-1]:
                if max_multi < multiply:
                    max_multi = multiply
                    max_i = i
                    max_j = j

print(max_i, 'x', max_j, '=', max_multi)

