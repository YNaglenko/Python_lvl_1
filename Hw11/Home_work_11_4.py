# 4) Напишите программу, которая найдет самое длинное слово в текстовом
# файле.

def longest_word_in_file(filename):
    longest_word = ""
    max_length = 0
    i_file = open(filename, "r")
    for txt in i_file:
        txt_string = i_file.readline()
        words_array = txt_string.split(" ")
        for word in words_array:
            if len(word) > max_length:
                max_length = len(word)
                longest_word = word
    return longest_word, max_length


result = longest_word_in_file("search_for_letter.txt")
print("The longest word in file is:", result[0], "with", result[1], "letters")
