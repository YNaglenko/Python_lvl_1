# 2)  Напишите  программу,  которая  вычитает  текст  из  текстового  файла  и
# выведет на экран, сколько раз в тексте встречается буква «A».

def search_letter_in_file(filepath, search):
    file_txt = open(filepath, "r")
    count = 0
    for txt in file_txt:
        for letter in txt:
            if letter == search:
                count = count + 1
    return count


print(search_letter_in_file("search_for_letter.txt", "A"))
