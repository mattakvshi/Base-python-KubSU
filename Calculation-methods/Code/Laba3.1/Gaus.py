def gauss(matrix, erf_list):
    n = len(matrix)

    # Прямой ход
    for i in range(n):

        # Находим максимальный элемент в столбце
        max_element = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_element:
                max_element = abs(matrix[k][i])
                max_row = k

        # Меняем строки местами
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        erf_list[i], erf_list[max_row] = erf_list[max_row], erf_list[i]

        # Обнуляем элементы
        for k in range(i + 1, n):
            c = -matrix[k][i] / matrix[i][i]
            for j in range(i, n):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]
            erf_list[k] += c * erf_list[i]

    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = erf_list[i] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            erf_list[k] -= matrix[k][i] * x[i]

    return x

def small_error(x, matrix, answ_list, x_list):
    res = 0
    for j in range(len(matrix[x - 1])):
        res += matrix[x - 1][j] * x_list[j]
    res -= answ_list[x - 1]
    return abs(res)

def task_a():
    matrix = [[0.0001, 1], [1, 2]]
    answ_list = [1, 4]
    x1, x2 = gauss(matrix, answ_list)
    x_list = [x1, x2]
    print("Задача а): Х1 = {}, Х2 = {}".format(round(x1, 5), round(x2, 5)))
    print("Невязки (по строкам): 1 = {}, 2 = {}".format(small_error(1, matrix, answ_list, x_list), small_error(2, matrix, answ_list, x_list)))

def task_b():
    matrix = [[2.34, -4.21, -11.61], [8.04, 5.22, 0.27], [3.92, -7.99, 8.37]]
    answ_list = [14.41, -6.44, 55.56]
    x1, x2, x3 = gauss(matrix, answ_list)
    x_list = [x1, x2, x3]
    print("Задача б): Х1 = {}, Х2 = {}, Х3 = {}".format(round(x1, 5), round(x2, 5), round(x3, 5)))
    print("Невязки (по строкам): 1 = {}, 2 = {}, 3 = {}".format(small_error(1, matrix, answ_list, x_list), small_error(2, matrix, answ_list, x_list), small_error(3, matrix, answ_list, x_list)))

def task_c():
    matrix = [[4.43, -7.21, 8.05, 1.23, -2.56], [-1.29, 6.47, 2.96, 3.22, 6.12], [6.12, 8.31, 9.41, 1.78, -2.88], [-2.57, 6.93, -3.74, 7.41, 5.55], [1.46, 3.62, 7.83, 6.25, -2.35]]
    answ_list = [2.62, -3.97, -9.12, 8.11, 7.23]
    x1, x2, x3, x4, x5 = gauss(matrix, answ_list)
    x_list = [x1, x2, x3, x4, x5]
    print("Задача в): X1 = {}, X2 = {}, X3 = {}, X4 = {}, X5 = {}".format(round(x1, 5), round(x2, 5), round(x3, 5), round(x4, 5), round(x5, 5)))
    print("Невязки (по строкам): 1 = {}, 2 = {}, 3 = {}, 4 = {}, 5 = {}".format(small_error(1, matrix, answ_list, x_list), small_error(2, matrix, answ_list, x_list), small_error(3, matrix, answ_list, x_list), small_error(4, matrix, answ_list, x_list), small_error(5, matrix, answ_list, x_list)))

def start():
    task_a()
    print()
    task_b()
    print()
    task_c()

start()