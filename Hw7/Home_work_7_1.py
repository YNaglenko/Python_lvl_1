week_dict = {1: "Monday",
             2: "Tuesday",
             3: "Wednesday",
             4: "Thursday",
             5: "Friday",
             6: "Saturday",
             7: "Sunday"}
day_num = int(input("Enter number of day: "))
week_day = week_dict.get(day_num)
if week_day is not None:
    print("You entered {dnum}, and it's {wd}".format(dnum=day_num, wd=week_day))
else:
    print("Sorry, your number of week day is out of range [1;7]")
