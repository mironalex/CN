import numpy as np

from hw2.lab2 import solve_system


def aitken(X, Y):
    y = list(Y)
    x = list(X)

    for k in range(1, len(x)):
        for i in reversed(range(k, len(y))):
            y[i] = y[i] - y[i - 1]

    h = x[1] - x[0]

    final_poly = [0] * len(y)
    final_poly[-1] = y[0]

    s = [1 / h, -x[0] / h]
    final_poly = np.polyadd(final_poly, np.polymul(s, y[1]))

    for k in range(2, len(y)):
        t_current = [(1 / h) / k, ((-x[0] / h) - k + 1) / k]
        s = np.polymul(s, t_current)

        final_poly = np.polyadd(final_poly, np.polymul(s, y[k]))

    return final_poly


def generate(n, x0, xn):
    h = (xn - x0) / n

    x = [x0]
    for i in range(1, n):
        x.append(x0 + i * h)
    x.append(xn)

    return x


def horner(x, poly):
    result = poly[0]
    for i in range(1, len(poly)):
        result *= x
        result += poly[i]

    return result


def squares_solve(X, Y):
    x = list(X)
    y = list(Y)

    x_mat = []
    for ln in range(len(x)):
        line = [1]
        for col in range(1, len(x)):
            line.append(line[-1] * x[ln])
        x_mat.append(line)

    k = 2

    Y = [sum(y)]
    for i in range(1, k + 1):
        sm = 0
        for j in range(len(y)):
            y[j] = y[j] * x[j]
            sm += y[j]

        Y.append(sm)

    x_sums = [len(x), sum(x)]
    x_pw = list(x)
    for i in range(1, 2 * k + 1):
        sm = 0
        for k in range(len(x)):
            x_pw[k] = x_pw[k] * x[k]
            sm += x_pw[k]

        x_sums.append(sm)

    X = []
    for i in range(k, 2 * k + 1):
        X.append(x_sums[i - k: i + 1])

    return np.linalg.solve(X, Y)


def test():
    f = lambda x: x * x - x + 1
    x0 = 1
    xn = 5
    n = 2

    x = generate(n, x0, xn)
    y = list(map(f, x))

    print(squares_solve(x, y))
    print(aitken(x, y))


if __name__ == '__main__':
    test()