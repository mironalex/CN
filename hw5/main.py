import numpy as np

epsilon = 10e-20
kmax = 1000


def get_solution_norm(A):
    max_sum_line = 0
    for i in range(0, len(A)):
        current_sum = 0
        for j in range(0, len(A)):
            current_sum += abs(A[i][j])
        if current_sum > max_sum_line:
            max_sum_line = current_sum
    return max_sum_line


def get_next_schultz(A, V):
    identity = 2 * np.identity(len(A))
    tmp = identity - np.matmul(A, V)
    return np.matmul(V, tmp)


def get_next_li1(A, V):
    identity = 3 * np.identity(len(A))
    AV = np.matmul(A, V)
    aux = np.matmul(AV, (identity - AV))
    return np.matmul(V, (identity - aux))


def get_next_li2(A, V):
    identity = np.identity(len(A))
    VA = np.matmul(V, A)
    aux1 = (1/4) * (identity - VA)
    aux2 = np.matmul((3 * identity - VA), (3 * identity - VA))
    return np.matmul((identity + np.matmul(aux1, aux2)), V)


def get_initial_matrix(A):
    transposed = np.transpose(A)
    max_sum_column = np.abs(A).sum(axis=0).max()
    max_sum_line = np.abs(A).sum(axis=1).max()
    return transposed / (max_sum_line * max_sum_column)


def generate_matrix(n):
    matrix = np.identity(n)
    for i in range(0, n-1):
        matrix[i, i+1] = 4
    return matrix


def solve(alg):
    A = generate_matrix(10)

    V_prev = V_next = get_initial_matrix(A)
    k = 0
    norm = 10e9
    while 10e10 >= norm >= epsilon and k < kmax:

        if alg == 1:
            V_next = get_next_schultz(A, V_prev)
        elif alg == 2:
            V_next = get_next_li1(A, V_prev)
        elif alg == 3:
            V_next = get_next_li2(A, V_prev)

        norm = np.linalg.norm(V_next - V_prev)
        k += 1
        V_prev = V_next
    print("\titerations = ", k)
    if norm < epsilon:
        print("\tconvergence")
        result_norm = get_solution_norm(np.matmul(A, V_next) - np.identity(len(A)))
        print("\tnorm = ", result_norm)
    else:
        print("\tdivergence\n")


if __name__ == '__main__':
    print("Schlutz: ")
    solve(1)
    print("Li 1: ")
    solve(2)
    print("Li 2: ")
    solve(3)
