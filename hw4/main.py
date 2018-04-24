from hw3 import sparse


epsilon = 10e-10


def calculate_norm(x, y):
    result = 0
    if len(x) != len(y):
        return None
    for i in range(0, len(x)):
        result += abs(x[i] - y[i])
    return result


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
    diag = [0] * n
    diag_contains_zero = False
    for i in range(0, n):
        for value in A.values[i]:
            j = value[1]
            if j == i and value[0] <= epsilon:
                diag_contains_zero = True
                break
            diag[i] = value[0]
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
        xGS = [0] * n
        for i in range(0, n):
            sum1 = 0
            sum2 = 0
            for j in range(0, len(A.values[i])):
                if A.values[i][j][1]-1 < i:
                    sum1 += A.values[i][j][0] * xGS[j]
                elif A.values[i][j][1]-1 > i:
                    sum2 += A.values[i][j][0] * x_prev[j]
            xGS[i] = (b[i] - sum1 - sum2)/diag[i]
        norm = calculate_norm(xGS, x_prev)
        print("\tnorm at iteration ", it, ": ", norm)
        it += 1
        x_prev = xGS
    print("done.")


if __name__ == "__main__":
    solve("m_rar_2018_1.txt")

