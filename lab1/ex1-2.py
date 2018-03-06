from random import random


def solve_ex1():
    u = 10
    m = 1
    prev = u
    while 1 + u != 1:
        u = pow(10, -m)
        m += 1
    return u


def solve_ex2():
    x = 1.0
    y = solve_ex1()
    z = y
    add_expression1 = (x + y) + z
    add_expression2 = x + (y + z)

    multiply_expression1 = 0
    multiply_expression2 = 0

    while(multiply_expression1 == multiply_expression2):
        x = random()/1000
        y = random()/1000
        z = random()/1000
        multiply_expression1 = (x * y) * z
        multiply_expression2 = x * (y * z)

    print("\nSolution for which multiplication is not associative:\n")
    print(x, y, z)
    return add_expression1 == add_expression2, multiply_expression1 == multiply_expression2


print(solve_ex1())
print(solve_ex2())