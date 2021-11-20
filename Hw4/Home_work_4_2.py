# 2) Вычислить с помощью цикла факториал числа n введенного с клавиатуры
# (4<n<16). Факториал числа - это произведение всех чисел от этого числа до 1.
# Например, 5!=5*4*3*2*1=120

number = int(input("Enter number "))
i = 1
factorial = number
if 4 < number < 16:
    while i < number:
        factorial = factorial * i
        i = i + 1
    print(number, '! = ', factorial)
else:
    print("Number is out of range between 4 and 16")


