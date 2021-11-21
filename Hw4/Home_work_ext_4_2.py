# С помощью циклов вывести на экран все простые числа от 1 до 100. Простое число
# —  число,  которое  делится  нацело  только  на  единицу  или  само  на  себя.  Первые
# простые числа это — 2,3,5,7…
#
# i = 2
# j = 1
# while i <= 10:
#     is_simple = 1
#     j = 1
#     while j <= 10:
#         if i % j == 0:
#             is_simple = 0
#             continue
#         #  print(i, j)
#         if is_simple == 1:
#             print(i)
#         j = j + 1
#     i += 1


i = 2
j = 2

while i <= 100:
    is_simple = 1
    j = 2
    while j < i:
        if i % j == 0:
            is_simple = 0
            break
        else:
            j = j + 1
    if is_simple == 1:
        print(i)
    i = i + 1

