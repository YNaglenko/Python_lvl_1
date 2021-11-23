# 4) Выведите на экран 10 строк со значением числа Pi. В первой строке должно быть
# 2 знака после запятой, во второй 3 и так далее.
import math
seq = 1
for i in range(2, 12):
    msg = "i - {sequence} pi = {p:.{i}f}".format(i=i, sequence = seq, p=math.pi)
    seq = seq + 1
    print(msg)
