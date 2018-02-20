import numpy as np


def four_way_slice(m, n):
    m11 = m[:n // 2, :n // 2]
    m12 = m[:n // 2, n // 2:]
    m21 = m[n // 2:, :n // 2]
    m22 = m[n // 2:, n // 2:]

    return m11, m12, m21, m22


def multiply_Strassen(a, b, n, n_min):
    if n <= n_min:
        return np.matmul(a, b)

    a11, a12, a21, a22 = four_way_slice(a, n)
    b11, b12, b21, b22 = four_way_slice(b, n)

    p1 = multiply_Strassen(a11 + a22, b11 + b22, n // 2, n_min)
    p2 = multiply_Strassen(a21 + a22, b11, n // 2, n_min)
    p3 = multiply_Strassen(a11, b12 - b22, n // 2, n_min)
    p4 = multiply_Strassen(a22, b21 - b11, n // 2, n_min)
    p5 = multiply_Strassen(a11 + a12, b22, n // 2, n_min)
    p6 = multiply_Strassen(a21 - a11, b11 + b12, n // 2, n_min)
    p7 = multiply_Strassen(a12 - a22, b21 + b22, n // 2, n_min)

    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 + p3 - p2 + p6

    c1 = np.concatenate([c11, c12], axis=1)
    c2 = np.concatenate([c21, c22], axis=1)
    return np.concatenate([c1, c2], axis=0)


if __name__ == '__main__':
    a = np.array([
        [-1, -2, -3, -4],
        [-5, -6, -7, -8],
        [-9, -10, -11, -12],
        [-13, -14, -15, -16]
    ])

    b = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])

    print(multiply_Strassen(a, b, 4, 2))
    print(np.matmul(a, b))