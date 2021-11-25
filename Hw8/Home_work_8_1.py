# 1)Напишите программу, которая считает две строки текста с клавиатуры и выведет
# на  экран  буквы,  которые  есть  одновременно  и  в  первой,  и  во  второй  строке.
# Например, для строк «Hello» и «World» на экране должны быть буквы «l» и «o».

txt_first = input("Enter the first string: ")
txt_second = input("Enter the second string: ")

set_first = set(txt_first)
set_second = set(txt_second)
common_letters = set_first.intersection(set_second)
msg = "\nFirst phrase: {ph1} \n Second phrase: {ph2}\n Common letters: {cl}".format(ph1=txt_first, ph2=txt_second,
                                                                                  cl=common_letters)
print(msg)
