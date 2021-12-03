def create_good(description, price):
    good = {"description": description,
            "price": price

            }
    return good


good1 = create_good("Apple", 25.75)
good2 = create_good("Banana", 10.01)
good3 = create_good("Milk", 25.40)
good_list = [good1, good2, good3]


def save_goods_to_file(good_l, file_addr):
    my_file = open(file_addr, 'w')
    for element in good_l:
        txt = str(element.get("description")) + ', ' + str(element.get("price"))
        my_file.write(txt + '\n')
    my_file.close()

save_goods_to_file(good_list,"good.csv")
