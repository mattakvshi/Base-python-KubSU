import numpy as np
import matplotlib.pyplot as plt

def jacobi_method(coeff_matrix, result_vector, initial_guess, tolerance):
    # Проверка размерности матрицы и вектора
    n = len(coeff_matrix)
    m = len(coeff_matrix[0])
    assert n == m, "Матрица коэффициентов должна быть квадратной"
    assert n == len(result_vector), "Размерности матрицы и вектора не совпадают"
    assert n == len(initial_guess), "Размерности матрицы и начального приближения не совпадают"

    # Инициализация переменных
    iteration = 0
    norm_residuals = []
    x = np.array(initial_guess)

    while True:
        # Вычисление нового приближения решения
        x_new = np.zeros(n)

        for i in range(n):
            sum_jacobi = 0
            for j in range(n):
                if j != i:
                    sum_jacobi += coeff_matrix[i][j] * x[j]

            x_new[i] = (result_vector[i] - sum_jacobi) / coeff_matrix[i][i]

        # Вычисление невязки и нормы невязки
        residual = np.dot(coeff_matrix, x) - result_vector
        norm_residual = np.linalg.norm(residual)

        # Добавление norm_residual в список для построения графика
        norm_residuals.append(norm_residual)

        # Проверка условия остановки по заданной точности
        if norm_residual < tolerance:
            break

        # Обновление решения
        x = x_new
        iteration += 1

    # Вывод результатов
    print("МЕТОД ЯКОБИ")
    print("Решение: ")
    print(x)
    print("График зависимости нормы невязки от номера итерации:")
    plt.plot(range(iteration + 1), norm_residuals)
    plt.xlabel("Номер итерации")
    plt.ylabel("Норма невязки")
    plt.title("МЕТОД ЯКОБИ")
    plt.show()
    print("Значение нормы невязки при достижении заданной точности ({:.6f}): {:.6f}".format(tolerance, norm_residual))


def gauss_seidel_method(coeff_matrix, result_vector, initial_guess, tolerance):
    # Проверка размерности матрицы и вектора
    n = len(coeff_matrix)
    m = len(coeff_matrix[0])
    assert n == m, "Матрица коэффициентов должна быть квадратной"
    assert n == len(result_vector), "Размерности матрицы и вектора не совпадают"
    assert n == len(initial_guess), "Размерности матрицы и начального приближения не совпадают"

    # Инициализация переменных
    iteration = 0
    norm_residuals = []
    x = np.array(initial_guess)

    while True:
        # Вычисление нового приближения решения
        x_new = np.zeros(n)

        for i in range(n):
            sum_seidel_1 = np.dot(coeff_matrix[i][:i], x_new[:i])
            sum_seidel_2 = np.dot(coeff_matrix[i][i + 1:], x[i + 1:])

            x_new[i] = (result_vector[i] - sum_seidel_1 - sum_seidel_2) / coeff_matrix[i][i]

        # Вычисление невязки и нормы невязки
        residual = np.dot(coeff_matrix, x) - result_vector
        norm_residual = np.linalg.norm(residual)

        # Добавление norm_residual в список для построения графика
        norm_residuals.append(norm_residual)

        # Проверка условия остановки по заданной точности
        if norm_residual < tolerance:
            break

        # Обновление решения
        x = x_new
        iteration += 1

    # Вывод результатов
    print("МЕТОД ЗЕЙДЕЛЯ")
    print("Решение: ")
    print(x)
    print("График зависимости нормы невязки от номера итерации:")
    plt.plot(range(iteration + 1), norm_residuals)
    plt.xlabel("Номер итерации")
    plt.ylabel("Норма невязки")
    plt.title("МЕТОД ЗЕЙДЕЛЯ")
    plt.show()
    print("Значение нормы невязки при достижении заданной точности ({:.6f}): {:.6f}".format(tolerance, norm_residual))


# Заданные значения
coeff_matrix = [[12.14, 1.32, -0.78, -2.75], [-0.89, 16.75, 1.88, -1.55], [2.65, -1.27, -15.64, -0.64],
                [2.44, 1.52, 1.93, -11.43]]
result_vector = [14.78, -12.14, -11.65, 4.26]
initial_guess = [0, 0, 0, 0] #Является начальным приближением к решению системы линейных уравнений
tolerance = 1e-4 #Допустимая погрешность результата вычислений (точность до 6 знаков после запятой)

# Решение СЛАУ методом Якоби
jacobi_method(coeff_matrix, result_vector, initial_guess, tolerance)

# Решение СЛАУ методом Зейделя
gauss_seidel_method(coeff_matrix, result_vector, initial_guess, tolerance)
