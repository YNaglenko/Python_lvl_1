# 4) Выведите на экран «песочные часы», максимальная ширина которых считывается с
# клавиатуры (число нечетное). В примере ширина равна 5.
# *****
#  ***
#    *
#  ***
# *****

w = int(input("Enter width: "))
if w % 2 != 0:
    ws = 0
    st = w

    while st > 1:
        print(ws * ' ', st * '*', ws * ' ')
        ws = ws + 1
        st = st - 2
    else:
        while st <= w:
            print(ws * ' ', st * '*', ws * ' ')
            ws = ws - 1
            st = st + 2

else:
    print("Number is even")
