# Представьте в виде списка списков матрицу
# [  1,  2 ,   3,   4]
# [  5,  6 ,   7,   8]
# [  9,10, 11, 12]
# [13,14, 15, 16]
# Напишите программу, которая выведет эту матрицу на экран, вычислит и выведет сумму
# элементов этой матрицы.
i = 1
matrix = []
total_sum = 0
for r in range(4):
    row = []
    for columns in range(4):
        row.append(i)
        i = i + 1
    matrix.append(row)

for element in matrix:
    print(element)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        total_sum = total_sum + matrix[i][j]
print('Total sum:', total_sum)




