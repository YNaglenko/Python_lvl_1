txt_string = input("Enter a string:")
l_string = len(txt_string)
min_word_size = len(txt_string)
word = txt_string
for i in range(min_word_size, 0, -1):
    sub_string = txt_string[:i]
    l_sub = len(sub_string)
    q_occur = txt_string.count(sub_string)
    if l_sub * q_occur == len(txt_string) and min_word_size > l_sub:
        word = sub_string
        min_word_size = l_sub
print(word)
