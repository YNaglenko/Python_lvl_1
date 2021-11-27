# Считайте  строку,  которая  будет  представлять  имя  человека,  введенное  с
# клавиатуры. Проверьте эту строку на валидность. Имеется в виду, что например, в
# имени человека не может быть цифр, оно должно начинаться с большой буквы, за
# которой должны следовать маленькие.

txt_name = input("Enter a name: ")
failed = 0
msg_error_txt = '\n'

if not txt_name.isalpha():
    failed = failed + 1
    msg_error_txt += 'Name must not contain any digit\n'

if not txt_name[0].isupper():
    msg_error_txt += 'Name must begin with UPPER case letter\n'
    failed = failed + 1

if not txt_name[1:].islower():
    msg_error_txt += 'All letters besides first must be in lower case\n'
    failed = failed + 1

if failed > 0:
    final_text = "Failed! You have {fails} validation error(s) and they are are: {txt}".format(fails=failed,
                                                                                               txt=msg_error_txt)
else:
    final_text = "Well done! The name \'{name}\' is valid".format(name=txt_name)

print(final_text)
