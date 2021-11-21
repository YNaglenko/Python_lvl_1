# 4) Выведите на экран «песочные часы», максимальная ширина которых считывается с
# клавиатуры (число нечетное). В примере ширина равна 5.
# *****
#  ***
#    *
#  ***
# *****

w = int(input("Enter width: "))
q_steps = (w // 2) + 1  # кількість ітерацій циклу

if w % 2 != 0:  # Якщо число не парне
    ws = 0      # пробіли
    st = w      # символи
    revers = 1  # коеф збільшення/ зменшення
    i = q_steps

    while i >= 0:
        print(ws * ' ', st * '*', ws * ' ')
        ws = ws + 1 * revers
        st = st - 2 * revers
        if st == 1:  # закінчення циклу зміюємо коеф. на -1
            revers = -1
            i = q_steps  # оновлюємо кількість ітераці
        i = i - 1
else:
    print("Number is even")

# Variant 2

# w = int(input("Enter width: "))
# if w % 2 != 0:
#     ws = 0
#     st = w
#
#     while st > 1:
#         print(ws * ' ', st * '*', ws * ' ')
#         ws = ws + 1
#         st = st - 2
#     else:
#         while st <= w:
#             print(ws * ' ', st * '*', ws * ' ')
#             ws = ws - 1
#             st = st + 2
#
# else:
#     print("Number is even")
