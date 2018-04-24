from hw3 import sparse


epsilon = 10e-10


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
            if value[1] == i and value[0] <= epsilon:
                diag_contains_zero = True
                break
        if diag_contains_zero:
            break

    print(filename, "result:\n")
    print("\tDiagonal contains zero: ", diag_contains_zero)
    if diag_contains_zero:
        return


solve("m_rar_2018_1.txt")
