import hw3.sparse as sparse
import time

a_matrix = sparse.SparseList()
b_matrix = sparse.SparseList()
aplusb_matrix = sparse.SparseList()
aorib_matrix = sparse.SparseList()
given_ax = []
given_bx = []
aplusbx = []
aoribx = []
epsilon = 10e-10

def init():
    with open('a.txt') as f:
        n = int(f.readline())
        f.readline()
        for i in range(0, n):
            given_ax.append(float(f.readline()))
        f.readline()
        for line in f:
            values = str.split(line, ",")
            a_matrix.insert(float(values[0]), int(values[1]), int(values[2]))

    with open('b.txt') as f:
        n = int(f.readline())
        f.readline()
        for i in range(0, n):
            given_bx.append(float(f.readline()))
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


def solve_mv_mult():
    v = list(range(2018, 0, -1))
    start = time.time()
    result_aoriv = v * a_matrix
    result_boriv = v * b_matrix
    end = time.time()
    print("\nM-V Multiplication Time Elapsed:", end - start)
    passed = True
    for i in range(0, len(result_aoriv)):
        if abs(result_aoriv[i] - given_ax[i]) > 10e-9:
            passed = False
            break
        if abs(result_boriv[i] - given_bx[i]) > 10e-9:
            passed = False
            break
    print("M-V test passed: ", passed)


init()
solve_aplusb()
solve_aorib()
solve_mv_mult()
