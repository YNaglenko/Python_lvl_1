def text_processing(filename, list_text):
    my_file = open(filename, "w")
    for element in list_text:
        my_file.write(element)
        my_file.write("\n")
    my_file.close()
    print("File is ready")


input_file_name = input("Введіть ім'я файлу: ")
print("Введіть текст, для завершення введення введіть q та натисніть Enter\n")
txt_list = []
input_string = ""
while input_string.lower() != "q":
    input_string = input(">")
    if input_string.lower() == "q":
        break
    else:
        txt_list.append(input_string)


text_processing(input_file_name, txt_list)
