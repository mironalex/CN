import numpy
from hw3 import sparse
import random
import numpy as np

epsilon = 10e-9
max_iterations = 10e5


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
        f.readline()
        f.readline()

        for line in f:
            values = str.split(line, ",")
            result.insert(float(values[0]), int(values[1]), int(values[2]))
    return result


def is_symmetric(input_matrix: sparse.SparseList):
    transposed = input_matrix.get_transposed()
    if input_matrix == transposed:
        return True
    return False


def power_method(input_matrix: sparse.SparseList):
    n = len(input_matrix.values)
    v = generate_random_initial_vector(n).tolist()
    w = v * input_matrix
    lambda_current = np.dot(w, v)
    iteration = 0
    while iteration < max_iterations:
        v = np.multiply(1 / np.linalg.norm(w), w)
        w = v.tolist() * input_matrix
        lambda_current = np.dot(w, v)
        iteration += 1
        norm = np.linalg.norm(w - (np.multiply(lambda_current, v)))
        if norm < n*epsilon:
            break
    print("\tIterations = ", iteration)
    return lambda_current


def get_matrix_rank(singular_values):
    rank = 0
    for value in singular_values:
        if value > epsilon:
            rank += 1
    return rank


def get_condition_number(singular_values):
    minimum_singular_value = 10e9
    maximum_singular_value = epsilon
    for value in singular_values:
        if epsilon < value < minimum_singular_value:
            minimum_singular_value = value
        if maximum_singular_value < value:
            maximum_singular_value = value
    return maximum_singular_value / minimum_singular_value


def get_pseudo_inverse(svd):
    u, s, v = svd
    si = np.zeros((u.shape[0], v.shape[0]))
    for i in range(len(s)):
        if s[i] < 0:
            break
        si[i, i] = 1/s[i]
    return np.matmul(np.matmul(u.T, si), v)


if __name__ == '__main__':
    # Task 1 and 2
    # print("Power method on random rare matrix:")
    # random_rare_matrix = generate_symmetric_rare_matrix(501)
    # print("\tResult:", power_method(random_rare_matrix))
    # print("Power method on given rare matrix:")
    # matrix = read_sparse_matrix("m_rar_sim_2018.txt")
    # print("\tIs symmetric:", is_symmetric(matrix))
    # print("\tResult: ", power_method(matrix))

    # Task 3
    random.seed(14058714618)
    random_matrix = numpy.random.rand(300, 200)
    print("Singular values:")
    svd = numpy.linalg.svd(random_matrix)
    print(svd[1])
    print("Matrix rang:")
    rang = get_matrix_rank(svd[1])
    print("\t", rang)
    print("Condition number:")
    print("\t", get_condition_number(svd[1]))
    print("Pseudo inverse:")
    print("\t", get_pseudo_inverse(svd))

    u, s, v = svd
    nr_s = rang + 1
    while nr_s > rang:
        nr_s = int(input("Enter number s (<= " + str(rang) + "): "))
    As = None
    for col in range(nr_s):
        u_col = u[0:u.shape[0], col]
        u_col = np.expand_dims(u_col, 1)

        v_col = v[0:v.shape[0], col]
        v_col = v_col[np.newaxis]

        temp = np.matmul(u_col, v_col)
        temp = temp * s[col]
        if As is None:
            As = temp
        else:
            As = As + temp
    print("||A - As|| =", np.linalg.norm(random_matrix - As))
