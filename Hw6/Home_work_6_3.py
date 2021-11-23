# 3) Напишите программу, которая вычислит сумму всех кодов символов строки.
txt_string = input("Enter string: ")
sum_codes = 0
for letter in txt_string:
    sum_codes += ord(letter)
    print(ord(letter))
msg = "You entered \'{txt}\' string, it's sum of ASCII/UTF-8 codes is {scodes}".format(txt=txt_string, scodes=sum_codes)
print(msg)
