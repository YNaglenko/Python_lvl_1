import random as rnd

lst_salary = []
salary_total = 0
avg_salary = 0
q_month = 12

for i in range(q_month):
    lst_salary.append(rnd.randint(7500, 15000))
    salary_total = salary_total + lst_salary[i]
avg_salary = salary_total / len(lst_salary)

print('Місяць', '\t', 'Сума, грн.')
for i in range(q_month):
    print(i + 1, '-', '\t', lst_salary[i])

print('Загальна сума, грн:', salary_total)
print('Средняя сума, грн:', round(avg_salary, 2))
