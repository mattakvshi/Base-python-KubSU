
def solve_gauss_method(coeff_matrix, result_vector):
    size = len(coeff_matrix)

    # шаг прямого хода
    for idx in range(size):
        # ищем максимальный элемент в столбце и запоминаем его
        max_elem = abs(coeff_matrix[idx][idx])
        max_row = idx
        for line in range(idx + 1, size):
            if abs(coeff_matrix[line][idx]) > max_elem:
                max_elem = abs(coeff_matrix[line][idx])
                max_row = line

        # меняем местами строки, ставя наибольший элемент на диагональ
        coeff_matrix[idx], coeff_matrix[max_row] = coeff_matrix[max_row], coeff_matrix[idx]
        result_vector[idx], result_vector[max_row] = result_vector[max_row], result_vector[idx]

        # обнуляем элементы столбца под главной диагональю
        for row in range(idx + 1, size):
            ratio = -(coeff_matrix[row][idx] / coeff_matrix[idx][idx])
            for column in range(idx, size):
                if idx == column:
                    coeff_matrix[row][column] = 0
                else:
                    coeff_matrix[row][column] += ratio * coeff_matrix[idx][column]
            result_vector[row] += ratio * result_vector[idx]

    # шаг обратного хода
    solution_vector = [0] * size
    for position in range(size - 1, -1, -1):
        solution_vector[position] = result_vector[position] / coeff_matrix[position][position]
        for row in range(position - 1, -1, -1):
            result_vector[row] -= coeff_matrix[row][position] * solution_vector[position]

    # возвращаем вектор решений
    return solution_vector


# функция для расчета невязки (остатка ошибки)
def compute_residue(line_num, coeff_matrix, result_vector, solution_vector):
    residue = sum(
        coeff_matrix[line_num - 1][idx] * solution_vector[idx] for idx in range(len(coeff_matrix[line_num - 1]))) - \
              result_vector[line_num - 1]
    return abs(residue)



if __name__ == '__main__':
    dataset = [
        {
            'task': 'Задача A',
            'matrix': [[0.0001, 1], [1, 2]],
            'result': [1, 4]
        },
        {
            'task': 'Задача Б',
            'matrix': [[2.34, -4.21, -11.61], [8.04, 5.22, 0.27], [3.92, -7.99, 8.37]],
            'result': [14.41, -6.44, 55.56]
        },
        {
            'task': 'Задача В',
            'matrix': [[4.43, -7.21, 8.05, 1.23, -2.56], [-1.29, 6.47, 2.96, 3.22, 6.12],
                       [6.12, 8.31, 9.41, 1.78, -2.88], [-2.57, 6.93, -3.74, 7.41, 5.55],
                       [1.46, 3.62, 7.83, 6.25, -2.35]],
            'result': [2.62, -3.97, -9.12, 8.11, 7.23]
        }
    ]

    # решение систем уравнений и вывод результатов
    for exercise in dataset:
        solution = solve_gauss_method(exercise['matrix'], exercise['result'])
        print(f"\n{exercise['task']}: Решения = {[round(x, 5) for x in solution]}")
        for line_num in range(1, len(exercise['matrix']) + 1):
            print(
                f"Невязки: Строка {line_num} = {compute_residue(line_num, exercise['matrix'], exercise['result'], solution)}")
