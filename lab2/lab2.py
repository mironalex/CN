from functools import reduce
from lab1.ex12 import solve_ex1

import numpy as np
import random


def solve_diagonal_system(system, result):
    assert len(system.shape) == 2
    assert system.shape[0] == system.shape[1], "Must be a square matrix"

    solution = np.zeros((system.shape[1], 1))
    lines, columns = system.shape
    for idx in reversed(range(0, lines)):
        line_offset = reduce(lambda accumulator, comb: accumulator + comb[0] * comb[1],
                             zip(system[idx, idx + 1:], solution[idx + 1:, 0]),
                             0)

        solution[idx, 0] = (result[idx, 0] - line_offset) / system[idx][idx]

    return solution


def reduce_system(system, result, column=0):
    if column == system.shape[1]:
        return

    idx = column + system[column:, column].argmax()
    system[[column, idx]] = system[[idx, column]]
    result[[column, idx]] = result[[idx, column]]

    for line in range(column + 1, system.shape[0]):
        epsilon = solve_ex1()
        if -epsilon <= system[line, column] <= epsilon:
            continue

        normalization_factor = system[column, column] / system[line, column]
        system[line] *= normalization_factor
        system[line] -= system[column]

        result[line, 0] *= normalization_factor
        result[line, 0] -= result[column, 0]

    reduce_system(system, result, column=column + 1)


def solve_system(system, result):
    internal_system = np.copy(system)
    internal_result = np.copy(result)

    reduce_system(internal_system, internal_result)
    return solve_diagonal_system(internal_system, internal_result)


def generate_random_system(size):
    system = []
    for i in range(0, size):
        current_line = []
        for j in range(0, size):
            current_line.append(random.random() * 10)
        system.append(current_line)

    result = []
    for i in range(0, size):
        result.append([random.random() * 10])
    return np.array(system), result


def flip(vali_list):
    result = []
    for x in vali_list:
        result.append(x[0])
    return result


if __name__ == '__main__':
    sys_result_pair = generate_random_system(100)

    system = sys_result_pair[0]
    result = sys_result_pair[1]

    try:
        determinant = np.linalg.det(system)
        if determinant == 0:
            raise ValueError("Error: Determinant is 0")
    except ValueError as error:
        print(repr(error))
        exit(1)

    solution = solve_system(
        system,
        result
    )

    np_solution = np.linalg.solve(system, result)

    """
    print("Solution =", solution)
    print("NP Solution =", np_solution)
    """

    solution_norm = solution - np_solution
    print("Norma solutia noastra - solutia biblioteca =", np.linalg.norm(solution_norm))

    solution_mul_sys = np.matmul(system, solution) - result
    print("Norma solutia noastra * sistemul - rezultatul =", np.linalg.norm(solution_mul_sys))

    np_solution_mul_sys = np.matmul(system, np_solution) - result
    print("Norma solutia biblioteca * sistemul - rezultatul =", np.linalg.norm(np_solution_mul_sys))
    """
    solution_result = np.matmul(system, solution)
    print("A * x_sol =", solution_result)
    print("Result = ", result)
    print("Norm: ", np.linalg.norm(result - solution_result))
    """
