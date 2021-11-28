def create_good(*args, serial_num, price):
    good = {"des": args,
            "serial_num": serial_num,
            "price": price
            }
    return good


good1 = create_good('red Apple', 44, serial_num=124454, price=20.75)
good3 = create_good('Onion', 60, serial_num=124455, price=7.50)
good2 = create_good('Carrot', 10, serial_num=124456, price=5.20)


def get_max_price(*goods):
    max_p = goods[0]
    for g in goods:
        if g.get("price") > max_p.get("price"):
            max_p = g
    return max_p


print(get_max_price(good1, good2, good3))
