import hw3.sparse as sparse
import time

a_matrix = sparse.SparseList()
b_matrix = sparse.SparseList()
aplusb_matrix = sparse.SparseList()
ax = []
bx = []
abx = []


def solve_aplusb():
    with open('a.txt') as f:
        n = int(f.readline())
        f.readline()
        for i in range(0, n):
            ax.append(float(f.readline()))
        f.readline()
        for line in f:
            values = str.split(line, ",")
            a_matrix.insert(float(values[0]), int(values[1]), int(values[2]))

    with open('b.txt') as f:
        n = int(f.readline())
        f.readline()
        for i in range(0, n):
            bx.append(float(f.readline()))
        f.readline()
        for line in f:
            values = str.split(line, ",")
            b_matrix.insert(float(values[0]), int(values[1]), int(values[2]))

    with open('aplusb.txt') as f:
        n = int(f.readline())
        f.readline()
        for i in range(0, n):
            abx.append(float(f.readline()))
        f.readline()
        for line in f:
            values = str.split(line, ",")
            aplusb_matrix.insert(float(values[0]), int(values[1]), int(values[2]))

    start = time.time()
    result_aplusb = a_matrix + b_matrix
    end = time.time()
    print(end - start)
    print(result_aplusb == aplusb_matrix)

solve_aplusb()
