h = int(input('Enter hight '))
w = int(input('Enter width '))


i = 1
j = 1

while i <= h:
    j = 1
    while j <= w:
        if i == 1 or j == 1 or i == h or j == w:  # межі фігури
            print('*', end='')
        else:
            print(' ', end='')
        j = j + 1
    print()
    i = i + 1

