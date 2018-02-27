from functools import reduce

import numpy as np


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
        # TODO: epsilon division instead of skipping
        if system[line, column] == 0:
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

# TODO: random generation

if __name__ == '__main__':
    system = np.array([
        [3.0, 2.0, 0.0],
        [6.0, 4.0, 0.0],
        [0.0, 1.0, 4.0],
    ])

    result = np.array([
        [12.0],
        [11.0],
        [10.0]
    ])

    # TODO: try catch for determinant 0
    solution = solve_system(
        system,
        result
    )

    # TODO: solutia noastra - solutia biblioteca - l2norm
    # TODO: solutia noastra * sistemul - resultatul - l2norm
    # TODO: solutia biblioteca * sistemul - resultatul - l2norm
    print("Solution =", solution)
    solution_result = np.matmul(system, solution)
    print("A * x_sol =", solution_result)
    print("Result = ", result)
    print("Norm: ", np.linalg.norm(result - solution_result))
