def get_factorial(n):
    if n > 1:
        return get_factorial(n - 1) * n
    else:
        return 1


f5 = get_factorial(5)
print(f5)
