from hw3 import sparse
import numpy as np

epsilon = 10e-10


def calculate_norm(x, y):
    if len(x) != len(y):
        return None
    return np.linalg.norm(np.asarray(x) - np.asarray(y))


def read_input(filename):
    A = sparse.SparseList()
    b = []
    with open(filename) as f:
        n = int(f.readline())
        f.readline()
        for i in range(0, n):
            b.append(float(f.readline()))
        f.readline()

        for line in f:
            values = str.split(line, ",")
            A.insert(float(values[0]), int(values[1]), int(values[2]))

    return n, A, b


def solve(filename):
    n, A, b = read_input(filename)
    diag_contains_zero = False
    for i in range(0, n):
        for value in A.values[i]:
            j = value[1]
            if j == i and value[0] <= epsilon:
                diag_contains_zero = True
                break
        if diag_contains_zero:
            break

    print(filename, "result:")
    print("\tDiagonal contains zero: ", diag_contains_zero)
    if diag_contains_zero:
        return

    x_prev = [0] * n
    xGS = []
    norm = 1
    it = 0
    while norm > epsilon:
        xGS = []
        for i in range(0, n):
            sum1 = 0
            sum2 = 0
            diag = 0
            for value, column in A.values[i]:
                if column < i:
                    sum1 += value * xGS[column]
                elif column > i:
                    sum2 += value * x_prev[column]
                elif column == i:
                    diag = value
            xGS.append((b[i] - sum1 - sum2) / diag)
        norm = calculate_norm(xGS, x_prev)
        print("\tnorm at iteration ", it, ": ", norm)
        it += 1
        x_prev = xGS
        if norm == float('Inf'):
            print("\tSolution Diverges")
            break

    print("\tIterations: ", it)
    solution_norm = calculate_norm(xGS * A, b)
    #test_norm = calculate_norm(([1.0] * n) * A, b)
    print("\tSolution Norm: ", solution_norm)
    #print("Test Norm: ", test_norm)
    print("done.")


if __name__ == "__main__":
    solve("m_rar_2018_1.txt")
    solve("m_rar_2018_2.txt")
    solve("m_rar_2018_3.txt")
    solve("m_rar_2018_4.txt")
    solve("m_rar_2018_5.txt")


