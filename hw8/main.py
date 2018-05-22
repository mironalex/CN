import math
import random
import inspect
from hw7.main import horner


def muller_x(poly, x, kmax=100000, eps=0.00001):
    x0, x1, x2 = x

    p_val0 = horner(poly, x0)
    p_val1 = horner(poly, x1)
    p_val2 = horner(poly, x2)

    k = 0
    dx = x2 - x1
    while k < kmax and abs(dx) >= eps and x2 < 100000000:
        h0 = x1 - x0
        h1 = x2 - x1

        d0 = (p_val1 - p_val0) / h0
        d1 = (p_val2 - p_val1) / h1

        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = p_val2

        sq2 = b * b - 4 * a * c
        if sq2 < 0:
            return None

        sq = math.sqrt(sq2)
        quotient = max(b + sq, b - sq)

        if abs(quotient) < eps:
            return None

        dx = 2 * c / quotient

        x0 = x1
        x1 = x2
        x2 = x2 - dx

        p_val0 = p_val1
        p_val1 = p_val2
        p_val2 = horner(poly, x2)

        k += 1

    if abs(dx) < eps:
        return x2
    return None


def muller(poly, kmax=1000, eps=0.00001):
    result = None
    while result is None:
        x0 = random.random()
        x1 = random.random()
        x2 = random.random()

        result = muller_x(poly, (x0, x1, x2), kmax=kmax, eps=eps)

    return result


def g(f, x, h=0.00001):
    if random.choice([1, 2]) == 1:
        return (3 * f(x) - 4 * f(x - h) + f(x - 2 * h)) / (2 * h)
    else:
        return (-1 * f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


def second_derivative(f, x, h=0.00001):
    return (-1 * f(x + 2 * h) + 16 * f(x + h) - 30 * f(x) + 16 * f(x - h) - f(x - 2 * h)) / (12 * h * h)


def sencanta_x(f, x, kmax=1000000, eps=0.000001):
    x0, x1 = x

    k = 0
    g0 = g(f, x0)
    g1 = g(f, x1)
    dx = x1 - x0

    while eps <= abs(dx) < 100000000 and k < kmax:
        if g0 == g1:
            dx = 0.00001
        else:
            dx = ((x1 - x0) * g1) / (g1 - g0)

        x0 =  x1
        x1 = x1 - dx

        g0 = g1
        g1 = g(f, x1)

        k += 1

    if abs(dx) < eps:
        return x1
    return None


def secanta(f, kmax=10000000, eps=0.00001):
    result = None
    while result is None:
        x0 = random.random()
        x1 = random.random()

        result = sencanta_x(f, (x0, x1), kmax=kmax, eps=eps)

    return result


def poly_str(poly):
    pw = len(poly) - 1
    poly_string = "lambda x: "
    first = True
    for coef in poly:
        if first:
            first = False
        else:
            poly_string += " + "

        poly_string += str(coef) + " * x**" + str(pw)
        pw -= 1

    return poly_string


def test():
    poly = [1, -4, 3]

    root = muller(poly)
    print("    f =", poly_str(poly))
    print("    root =", root)
    print("    f(root) =", horner(poly, root))
    print("")

    f = lambda x: x * x + math.exp(x)
    x_min = secanta(f)

    print(inspect.getsource(f), end='')
    print("    - x_min =", x_min)
    print("    - first derivative =", g(f, x_min))
    print("    - second_derivative = ", second_derivative(f, x_min))


if __name__ == '__main__':
    test()