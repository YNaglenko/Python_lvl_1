my_file = open("a.txt", "w")
my_file.write("Python is cool")


my_list = [1, 3, 5, 8, 2]
for element in my_list:
    my_file.write(str(element))
    my_file.write("\n")

my_file.close()

my_file = open("a.txt", 'r')
text = my_file.read()
my_file.close()
print(text)