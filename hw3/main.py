import hw3.sparse as sparse

a_matrix = sparse.SparseList()
b_matrix = sparse.SparseList()
ax = []
bx = []


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



solve_aplusb()
