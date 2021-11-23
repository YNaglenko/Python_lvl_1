#  Вводится строка из слов, разделенных пробелами. Найти самое длинное слово и
# вывести его на экран.
txt_string = input("Enter a sentence: ")
delimited_txt = txt_string.split(" ")
longest_word = delimited_txt[0]
max_size_char = len(delimited_txt[0])
for element in delimited_txt:
    if max_size_char < len(element):
        longest_word = element
        max_size_char = len(element)
msg = "The longest word is {lw}, and it consists of {msc} char(s)".format(lw=longest_word, msc=max_size_char)
print(msg)
