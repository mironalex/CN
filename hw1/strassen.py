import numpy as np
import random

def four_way_slice(m, n):
    m11 = m[:n // 2, :n // 2]
    m12 = m[:n // 2, n // 2:]
    m21 = m[n // 2:, :n // 2]
    m22 = m[n // 2:, n // 2:]

    return m11, m12, m21, m22


def multiply_Strassen_pad(a, b, n, n_min):
    if n <= n_min:
        return np.matmul(a, b)

    a11, a12, a21, a22 = four_way_slice(a, n)
    b11, b12, b21, b22 = four_way_slice(b, n)

    p1 = multiply_Strassen_pad(a11 + a22, b11 + b22, n // 2, n_min)
    p2 = multiply_Strassen_pad(a21 + a22, b11, n // 2, n_min)
    p3 = multiply_Strassen_pad(a11, b12 - b22, n // 2, n_min)
    p4 = multiply_Strassen_pad(a22, b21 - b11, n // 2, n_min)
    p5 = multiply_Strassen_pad(a11 + a12, b22, n // 2, n_min)
    p6 = multiply_Strassen_pad(a21 - a11, b11 + b12, n // 2, n_min)
    p7 = multiply_Strassen_pad(a12 - a22, b21 + b22, n // 2, n_min)

    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 + p3 - p2 + p6

    c1 = np.concatenate([c11, c12], axis=1)
    c2 = np.concatenate([c21, c22], axis=1)
    return np.concatenate([c1, c2], axis=0)


def multiply_Strassen(a, b, n, n_min):
    assert a.shape[0] == a.shape[1], "a must be a square matrix"
    assert b.shape[0] == b.shape[1], "b must be a square matrix"
    assert a.shape[0] == b.shape[0], "a and b must have the same size"

    size = a.shape[0]
    pad_size = 1
    while pad_size < size:
        pad_size *= 2

    a_padded = np.zeros((pad_size, pad_size))
    a_padded[:size, :size] = a

    b_padded = np.zeros((pad_size, pad_size))
    b_padded[:size, :size] = b

    result = multiply_Strassen_pad(a_padded, b_padded, pad_size, n_min)

    return result[:size, :size]


def generate_random_matrix(size):
    matrix = []
    for i in range(0, size):
        current_line = []
        for j in range(0, size):
            current_line.append(random.random() * 10)
        matrix.append(current_line)
    return np.array(matrix)


if __name__ == '__main__':
    size = 100

    a = generate_random_matrix(size)

    b = generate_random_matrix(size)

    our_result = multiply_Strassen(a, b, size, 2)
    np_result = np.matmul(a, b)

    norm_matrix = our_result - np_result

    #print(multiply_Strassen(a, b, size, 2))
    #print(np.matmul(a, b))
    print("Norm =", np.linalg.norm(norm_matrix))
