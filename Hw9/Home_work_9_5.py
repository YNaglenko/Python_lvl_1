# Напишите функцию, которая вернет количество слов в строке текста.

def q_words(input_str):
    word_list = str(input_str).split(" ")
    qw = len(word_list)
    return qw


test_string = "The weather is fine now"

count_words = q_words(test_string)
print("Quantity of words in the phrase \'", test_string, "\' is:", count_words)
