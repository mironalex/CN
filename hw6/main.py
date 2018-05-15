from hw3 import sparse
import random
import numpy as np

epsilon = 10e-15
max_iterations = 10e7


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


def generate_random_initial_vector(n):
    result = []
    for i in range(0, n):
        value = (random.random() + epsilon) * 10
        result.append(value)
    result = np.multiply(1 / np.linalg.norm(result), result)
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


def is_symmetric(matrix: sparse.SparseList):
    transposed = matrix.get_transposed()
    if matrix == transposed:
        return True
    return False


def power_method(matrix: sparse.SparseList):
    n = matrix.rows+1
    v = generate_random_initial_vector(n).tolist()
    w = v * matrix
    lambda_current = np.dot(w, v)
    iteration = 0
    while iteration < max_iterations and np.linalg.norm(w - lambda_current) < n*epsilon:
        v = np.multiply(1 / np.linalg.norm(w), w)
        w = v * matrix
        lambda_current = np.dot(w, v)
        iteration += 1
    return lambda_current


if __name__ == '__main__':
    random_rare_matrix = generate_symmetric_rare_matrix(501)
    print(power_method(random_rare_matrix))

    input_matrix = read_sparse_matrix("m_rar_sim_2018.txt")
    print(is_symmetric(input_matrix))
    print(power_method(input_matrix))
