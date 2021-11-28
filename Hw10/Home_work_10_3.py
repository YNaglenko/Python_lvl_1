# Напишите программу, которая попросит ввести пользователя его имя и возраст.
# После проверки возраста на корректность (чтобы не был меньше 0 и больше 500)
# выведите имя человека и его возрастную градацию:
# 0-10 — детский возраст, 10-25 - юный возраст, от 25 до 44 лет - молодой возраст,
# 44-60 лет - средний возраст, 60-75 лет - пожилой возраст, 75-90 лет -  старческий
# возраст, а после 90 - долгожитель.


def calc_age_range(age, name):
    if 0 <= age <= 500:
        age_reference = {10: "дитячий вік", 25: "юний вік",
                         44: "молодий вік", 60: "середній вік",
                         75: "похилий вік", 90: "довгожитель"}
        age_description = age_reference.get(90)
        for key in age_reference.keys():
            if age < key:
                age_description = age_reference.get(key)
                break
            else:
                continue
        msg = "{n} віком {a} - має {ad}".format(n=name, a=age, ad=age_description)
    else:
        msg = "Помилка у вказаному віці. Вік {a} не належить діапазону від 0 до 500".format(a=age)
    return msg


name_user = input("Enter name: ")
age_user = int(input("Enter age: "))
answer = calc_age_range(age=age_user, name=name_user)
print(answer)
