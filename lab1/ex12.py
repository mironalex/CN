from random import random
from random import randint
import time


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
    iterations = 0
    while multiply_expression1 == multiply_expression2:
        iterations += 1
        x = random() / 1000
        y = random() / 1000
        z = random() / 1000
        multiply_expression1 = (x * y) * z
        multiply_expression2 = x * (y * z)

    print("\nSolution for which multiplication is not associative:\n")
    print("\tFound in: ", iterations, " iterations\n")
    print("\t", x, y, z, "\n")
    return add_expression1 == add_expression2, multiply_expression1 == multiply_expression2


def compare_efficiency():
    time_sum = 0
    time_mul = 0
    iterations = 1000000
    start_sum = time.clock()

    for i in range(0, iterations):
        randint(100, 100000) + randint(100, 100000)

    time_sum = time.clock() - start_sum

    start_mul = time.clock()

    for i in range(0, iterations):
        randint(100, 100000) * randint(100, 100000)

    time_mul = time.clock() - start_mul

    print("Time elapsed sum:", time_sum)
    print("Time elapsed mul:", time_mul)


if __name__ == "__main__":
    compare_efficiency()
