# Напишите  программу  которая  считает  строку  текста  с  клавиатуры  и  выведет  на
# экран статистику, сколько раз какая буква встречается  в этой строке.  Например,
# для строки «Hello world» эта статистика выглядит, как: «H» - 1 , «e» - 1, «l» - 3 и т.д.

txt_string = input("Enter a txt string: ")
txt_parts = {}
for letter in txt_string:
    qnty = txt_parts.get(letter)
    if qnty is None:
        txt_parts[letter] = 1
    else:
        txt_parts[letter] = qnty + 1

for key in txt_parts.keys():
    print(key, '-', txt_parts[key])
