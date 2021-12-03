def num_list_to_file(list_numbers, filepath):
    csv_file = open(filepath, "w")
    csv_file.write("value" + "\n")  # add table header
    for i in range(len(list_numbers)):
        csv_file.write(str(list_numbers[i]) + "\n")
    print("File is ready")


list_one = [1, 3, 5, 7, 9, 45, 142, 54540, 545]
num_list_to_file(list_numbers=list_one, filepath="list.csv")
