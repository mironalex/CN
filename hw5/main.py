import numpy as np

epsilon = 10e-10
kmax = 1000


def get_next_schultz(A, V):
    identity = 2 * np.identity(len(A))
    return np.multiply(V, identity - np.multiply(A, V))


def get_next_li1(A, V):
    identity = 3 * np.identity(len(A))
    AV = np.multiply(A, V)
    aux = np.multiply(AV, identity - AV)
    return np.multiply(V, identity - aux)


def get_next_li2(A, V):
    identity = np.identity(len(A))
    VA = np.multiply(V, A)
    aux1 = np.multiply(1/4, identity - VA)
    aux2 = np.multiply(3 * identity - VA, 3 * identity - VA)
    return np.multiply(identity + np.multiply(aux1, aux2), V)


def get_initial_matrix(A):
    return np.divide(np.transpose(A), np.linalg.norm(A, ord=2))


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
        print("\tdivergence")
        result_norm = np.linalg.norm(np.multiply(A, V_next) - np.identity((len(A))))
        print("\tnorm = ", result_norm)
    else:
        print("\tconvergence\n")


if __name__ == '__main__':
    print("Schlutz: ")
    solve(1)
    print("Li 1: ")
    solve(2)
    print("Li 2: ")
    solve(3)
