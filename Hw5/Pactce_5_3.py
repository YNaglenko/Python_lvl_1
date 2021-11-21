import random as rnd

the_matrix = []
tmp_list = []
for r in range(5):
    row = []
    for c in range(5):
        row.append(rnd.randint(1, 9))
    the_matrix.append(row)

for el in the_matrix:
    print(el)

summa = 0
for i in range(len(the_matrix)):
    summa = summa + the_matrix[i][i]
print(summa)

