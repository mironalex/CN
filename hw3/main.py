import hw3.sparse as sparse
import time

a_matrix = sparse.SparseList()
b_matrix = sparse.SparseList()
aplusb_matrix = sparse.SparseList()
aorib_matrix = sparse.SparseList()
ax = []
bx = []
aplusbx = []
aoribx = []


def init():
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
            aplusbx.append(float(f.readline()))
        f.readline()
        for line in f:
            values = str.split(line, ",")
            aplusb_matrix.insert(float(values[0]), int(values[1]), int(values[2]))

    with open('aorib.txt') as f:
        n = int(f.readline())
        f.readline()
        for i in range(0, n):
            aoribx.append(float(f.readline()))
        f.readline()
        for line in f:
            values = str.split(line, ",")
            aorib_matrix.insert(float(values[0]), int(values[1]), int(values[2]))


def solve_aplusb():
    start = time.time()
    result_aplusb = a_matrix + b_matrix
    end = time.time()
    print("\nAddition Time Elapsed: ", end - start)
    print("Addition test passed: ", result_aplusb == aplusb_matrix)


def solve_aorib():
    start = time.time()
    result_aorib = a_matrix * b_matrix
    end = time.time()
    print("\nM-M Multiplication Time Elapsed:", end - start)
    print("M-M test passed: ", result_aorib == aorib_matrix)


def solve_amatmulb():
    start = time.time()
    result_amatmulb = sparse.matmul(a_matrix, b_matrix)
    end = time.time()
    print("\nM-M matmul Multiplication Time Elapsed:", end - start)
    print("M-M matmul test passed: ", result_amatmulb == aorib_matrix)


init()
solve_aplusb()
solve_aorib()
solve_amatmulb()