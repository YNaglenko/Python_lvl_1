def print_rectangle(h, w):
    i = 1
    j = 1
    while i <= h:
        j = 1
        while j <= w:
            if i == 1 or j == 1 or i == h or j == w:
                print('*', end='')
            else:
                print(' ', end='')
            j = j + 1
        print()
        i = i + 1


print_rectangle(5, 7)
