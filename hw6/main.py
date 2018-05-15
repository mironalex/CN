from hw3 import sparse
import random

epsilon = 10e-10


def generate_symmetric_rare_matrix(n):
    result = sparse.SparseList()
    random_element_count = random.randint(n, n*5)
    for i in range(0, random_element_count):
        value = random.random() * 10
        line = random.randint(0, n)
        column = random.randint(0, n)
        result.insert(value, line, column)
        result.insert(value, column, line)
    return result


def read_sparse_matrix(filename):
    result = sparse.SparseList()
    with open(filename) as f:
        n = int(f.readline())
        f.readline()

        for line in f:
            values = str.split(line, ",")
            result.insert(float(values[0]), int(values[1]), int(values[2]))
    return result


if __name__ == '__main__':
    pass
