# 1) Напишите  программу,  которая  посчитает  сколько  букв  «b»  в  введенной  строке
# текста.

txt_string = input("Enter your text here: ")
count_b = 0
for i in range(len(txt_string)):
    if txt_string[i] == 'b':
        count_b = count_b + 1
print("Qnty of letter \'b\' is:", count_b)
