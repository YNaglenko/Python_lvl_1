def print_triangle(q_lines):
    q_space = q_lines
    q_stars = 0
    for i in range(q_lines):
        q_space = q_space - 1
        q_stars = i
        print(q_space * " ", end="")
        print(q_stars * "*", end="")
        print()


a = 10
print_triangle(a)
