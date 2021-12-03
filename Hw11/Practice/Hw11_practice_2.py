def search_in_file(fname, search1, search2):
    file_1 = open(fname, "r")
    string_s = file_1.read()
    file_1.close()
    search1_count = 0
    search2_count = 0
    for letter in string_s:
        if letter == search1:
            search1_count = search1_count + 1
        elif letter == search2:
            search2_count = search2_count + 1
    return search1_count, search2_count


z = search_in_file("practic2.txt", "A", "a")
print(z)
