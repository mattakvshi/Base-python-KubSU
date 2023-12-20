import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve  # Используем solve из scipy для решения СЛАУ


def explicit_scheme(dx, dt, T):
    """
    Реализация явной разностной схемы для решения уравнения.

    Аргументы:
    dx -- шаг по x
    dt -- шаг по t
    T  -- значение времени T

    Возвращает:
    u_explicit -- массив значений решения
    """
    # L - количество узлов по пространству x.
    L = int(np.pi / 2 / dx) + 1

    # N - количество временных шагов до достижения времени T.
    N = int(T / dt) + 1

    # np.linspace - создает равномерно распределенный массив точек от 0 до np.pi/2 включительно, всего L точек.
    x = np.linspace(0, np.pi / 2, L)

    # np.linspace - создает равномерно распределенный массив временных точек от 0 до T включительно, всего N точек.
    t = np.linspace(0, T, N)

    # Инициализация массива для хранения решения с нулевыми значениями для всех временных и пространственных шагов.
    u_explicit = np.zeros((N, L))

    # Установка начального условия: u(x,0) = sin(x) для всех x.
    u_explicit[0, :] = np.sin(x)

    # r - число Куранта, которое необходимо, чтобы определить устойчивость явной схемы.
    # Этот параметр должен быть меньше или равен 0.5 для устойчивости схемы.
    r = dt / dx ** 2

    # Проверка условия устойчивости схемы.
    if r > 0.5:
        print("WARNING: Условие устойчивости не выполнено. Результаты могут быть неточными.")

    # Основной цикл по времени (от 0 до N - 1).
    for n in range(N - 1):
        # Вложенный цикл по пространству x (от 1 до L - 2, края не рассчитываем).
        for i in range(1, L - 1):
            # Обновление значений в узлах по явной схеме учитывая соседние узлы.
            u_explicit[n + 1, i] = (1 - 2 * r) * u_explicit[n, i] + r * (u_explicit[n, i - 1] + u_explicit[n, i + 1])

        # Установка граничного условия u(np.pi/2, t) = e^(-t) в последнем узле пространственной сетки на каждом временном шаге.
        u_explicit[n + 1, -1] = np.exp(-t[n + 1])

    # Возвращение массива решений после выполнения всех итераций.
    return u_explicit


def implicit_scheme(dx, dt, T):
    """
    Реализация неявной разностной схемы для решения уравнения.

    Аргументы:
    dx -- шаг по x
    dt -- шаг по t
    T -- значение времени T

    Возвращает:
    u_implicit -- массив значений решения
    """
    L = int(np.pi / 2 / dx) + 1
    '''
    Определение числа узлов сетки по пространству. Пространственный интервал делится от 0 до pi/2, 
    и далее округляется до целого числа. Поскольку на конце интервала требуется узел, добавляется единица.
    '''

    N = int(T / dt) + 1
    '''
    Определение числа временных слоёв. Временной интервал делится на шаги dt и округляется до целого числа. 
    Здесь также добавляется единица, чтобы включить и начальное и конечное значения времени.
    '''

    x = np.linspace(0, np.pi / 2, L)
    '''
    Генерация равномерно распределенного массива значений x от 0 до pi/2, содержащего L элементов.
    '''

    t = np.linspace(0, T, N)
    '''
    Генерация равномерно распределенного массива значений t от 0 до T, содержащего N элементов.
    '''

    u_implicit = np.zeros((N, L))
    '''
    Инициализация двумерного массива u_implicit размером N на L, который изначально заполняется нулями. 
    Этот массив будет хранить значения искомой функции во всех временных и пространственных точках.
    '''
    u_implicit[0, :] = np.sin(x)
    '''
    Задание начального условия: искомая функция в начальный момент времени (при t = 0) равна синусу от соответствующего x.
    '''

    r = dt / dx ** 2
    '''
    Расчет параметра r, который широко используется в разностных схемах и выражает соотношение между временным шагом и квадратом пространственного шага.
    '''

    A = np.zeros((L - 2, L - 2))
    A[range(L - 2), range(L - 2)] = 1 + 2 * r
    A[range(L - 3), range(1, L - 2)] = -r
    A[range(1, L - 2), range(L - 3)] = -r

    '''
    Создание матрицы A, которая используется при решении системы линейных уравнений. 
    Размер матрицы L-2 указывает на отсутствие граничных узлов, т.к. их значения уже известны из граничных условий.
    
    Диагональ матрицы A заполняется значениями 1 + 2*r, 
    что является частью разностного аналога второй пространственной производной в уравнении теплопроводности.
    
    Две соседние с главной диагонали линии (верхняя и нижняя) заполняются значениями -r. 
    Это представляет связь между соседними узлами по пространству.
    '''

    for n in range(N - 1):
        b = u_implicit[n, 1:L - 1].copy()
        b[0] += r * u_implicit[n + 1, 0]
        b[-1] += r * u_implicit[n + 1, -1]

        u_implicit[n + 1, 1:L - 1] = np.linalg.solve(A, b)
        u_implicit[n + 1, 0] = 0
        u_implicit[n + 1, -1] = np.exp(-t[n + 1])

    '''
    Цикл по временным слоям, который не включает последний момент времени, так как начальное время уже заполнено.

    Создание временного массива b, который содержит значения искомой функции 
    на текущем временном слое без учёта граничных точек. Создается копия, чтобы избежать изменения исходных данных.

    Корректировка первого и последнего элементов массива b, учитывая граничные условия (значения в следующий момент времени).
    
    Решение системы линейных алгебраических уравнений A * u = b для нахождения значений искомой функции на следующем временном слое.
    
    Применение граничных условий: на левой границе устанавливается значение 0, 
    на правой границе значение искомой функции изменяется в соответствии с exp(-t) в следующий момент времени t[n + 1].
    '''

    return u_implicit


# def implicit_scheme(dx, dt, T):
#     """
#     Интегрированная реализация неявной разностной схемы.
#
#     Аргументы:
#     dx -- шаг по x
#     dt -- шаг по t
#     T -- значение времени T до которого будет проводиться расчет
#
#     Возвращает:
#     u_implicit -- массив значений решения
#     """
#
#     L = int(np.pi / 2 / dx) + 1  # Число шагов по пространству
#     N = int(T / dt) + 1  # Число шагов по времени
#
#     x = np.linspace(0, np.pi / 2, L)
#     t = np.linspace(0, T, N)
#
#     u_implicit = np.zeros((N, L))  # Инициализация сетки нулями
#     u_implicit[0, :] = np.sin(x)  # Начальное условие u(x, 0) = sin(x)
#
#     r = dt / dx ** 2  # Параметр стабильности
#
#     # Коэффициенты для tridiagonal matrix algorithm (TDMA), также известный как алгоритм Томаса
#     A_diag = -(1 + 2 * r) * np.ones(L - 2)  # Основная диагональ матрицы A
#     off_diag = r * np.ones(L - 3)  # Верхняя и нижняя диагонали матрицы A
#
#     # Модифицируем коэффициенты для учета граничных условий
#     A = np.diag(A_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
#
#     for k in range(1, N):
#         # Инициализируем вектор правой части уравнения
#         b = np.zeros(L - 2)
#         for i in range(1, L - 1):
#             b[i - 1] = -r * (u_implicit[k - 1, i + 1] - 2 * u_implicit[k - 1, i] + u_implicit[k - 1, i - 1])
#
#         # Применяем граничные условия
#         b[0] -= r * u_implicit[k - 1, 0]  # при i = 1 (из-за Python индексы начинаются с 0)
#         b[-1] -= r * np.exp(-t[k])  # при i = L - 2
#
#         # Решаем систему линейных алгебраических уравнений Ax = b
#         u_implicit[k, 1:-1] = solve(A, b)
#         u_implicit[k, 0] = 0  # Граничное условие u(0, t) = 0
#         u_implicit[k, -1] = np.exp(-t[k])  # Граничное условие u(pi/2, t) = exp(-t)
#
#     return u_implicit


# def implicit_scheme(dx, dt, T):
#     """
#     #     Интегрированная реализация неявной разностной схемы.
#     #
#     #     Аргументы:
#     #     dx -- шаг по x
#     #     dt -- шаг по t
#     #     T -- значение времени T до которого будет проводиться расчет
#     #
#     #     Возвращает:
#     #     u_implicit -- массив значений решения
#     #     """
#     L = int(np.pi / 2 / dx) + 1  # Число шагов по пространству
#     N = int(T / dt) + 1  # Число шагов по времени
#
#     x = np.linspace(0, np.pi / 2, L)
#     t = np.linspace(0, T, N)
#
#     u_implicit = np.zeros((N, L))  # Инициализация сетки нулями
#     u_implicit[0, :] = np.sin(x)  # Начальное условие u(x, 0) = sin(x)
#
#     r = dt / dx ** 2  # Параметр стабильности
#
#     # Инициализация коэффициентов для неявной схемы
#     a_implicit = -r * np.ones(L-1)  # Поддиагональ
#     b_implicit = (1 + 2 * r) * np.ones(L)  # Главная диагональ
#     c_implicit = -r * np.ones(L-1)  # Наддиагональ
#
#     # Метод прогонки (Томаса)
#     for k in range(1, N):
#         d = u_implicit[k-1, :].copy()  # Правая часть уравнения
#         d[0] = 0  # Граничное условие u(0, t) = 0
#         d[-1] = np.exp(-t[k])  # Граничное условие u(pi/2, t) = exp(-t)
#
#         # Прямой проход метода прогонки
#         for i in range(1, L):
#             w = a_implicit[i-1] / b_implicit[i-1]
#             b_implicit[i] -= w * c_implicit[i-1]
#             d[i] -= w * d[i-1]
#
#         # Обратный проход метода прогонки
#         u_implicit[k, L-1] = d[-1] / b_implicit[-1]
#         for i in range(L-2, -1, -1):
#             u_implicit[k, i] = (d[i] - c_implicit[i] * u_implicit[k, i+1]) / b_implicit[i]
#
#     return u_implicit

def plot_solutions(x, t, u_explicit, u_implicit, exact_solution):
    """
    Построение графиков решений.

    Аргументы:
    x -- массив значений x
    t -- массив значений t
    u_explicit -- массив значений решения для явной схемы
    u_implicit -- массив значений решения для неявной схемы
    exact_solution -- массив значений точного решения
    """
    X, T = np.meshgrid(x, t)

    fig = plt.figure(figsize=(10, 6))

    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.plot_surface(X, T, u_explicit, cmap='viridis')
    ax1.set_xlabel('x')
    ax1.set_ylabel('t')
    ax1.set_zlabel('u')
    ax1.set_title('Явная схема')

    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    ax2.plot_surface(X, T, u_implicit, cmap='viridis')
    ax2.set_xlabel('x')
    ax2.set_ylabel('t')
    ax2.set_zlabel('u')
    ax2.set_title('Неявная схема')

    fig2, axs = plt.subplots(1, 3, figsize=(15, 5))

    # график явной схемы
    axs[0].plot(x, u_explicit[-1], label='Явная схема')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('u')
    axs[0].set_title('Явная схема в последний момент времени')
    axs[0].legend()

    # график неявной схемы
    axs[1].plot(x, u_implicit[-1], label='Неявная схема')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('u')
    axs[1].set_title('Неявная схема в последний момент времени')
    axs[1].legend()

    # график сравнения явной и неявной схемы с точным решением
    axs[2].plot(x, u_explicit[-1], label='Явная схема')
    axs[2].plot(x, u_implicit[-1], label='Неявная схема')
    axs[2].plot(x, exact_solution, label='Точное решение')
    axs[2].set_xlabel('x')
    axs[2].set_ylabel('u')
    axs[2].set_title('Сравнение решений')
    axs[2].legend()

    plt.show()


def plot_temperature_solutions(x, t, net, net_analytical, scheme):
    """
    Построение графиков решений, аналогичных тем, что используются в коде друга.

    Аргументы:
    x -- массив значений x
    t -- массив значений t
    scheme -- название схемы
    net_analytical -- аналитическое решение сетки

    """
    # Преобразование списков в DataFrame
    net_df = pd.DataFrame(net)
    net_analytical_df = pd.DataFrame(net_analytical)

    figure = plt.figure(figsize=(18, 6))

    # График решения сетки
    ax1 = figure.add_subplot(1, 3, 1)
    sns.heatmap(net_df, cmap='viridis', xticklabels=round(len(x) / 10), yticklabels=round(len(t) / 10), ax=ax1)
    ax1.set_title(F'{scheme}')
    ax1.set_xlabel('Space (x)')
    ax1.set_ylabel('Time (t)')

    # График аналитического решения сетки
    ax2 = figure.add_subplot(1, 3, 2)
    sns.heatmap(net_analytical_df, cmap='viridis', xticklabels=round(len(x) / 10), yticklabels=round(len(t) / 10),
                ax=ax2)
    ax2.set_title('Точное решение')
    ax2.set_xlabel('Space (x)')
    ax2.set_ylabel('Time (t)')

    plt.tight_layout()
    plt.show()

def main():
    dx = np.pi / 60
    dt = 0.001
    T = 0.0001

    x = np.linspace(0, np.pi / 2, int(np.pi / 2 / dx) + 1)
    t = np.arange(0, T + dt, dt)

    u_exact = np.exp(-t[:, np.newaxis]) * np.sin(x)

    u_explicit = explicit_scheme(dx, dt, T)
    u_implicit = implicit_scheme(dx, dt, T)

    # Вычислите абсолютные ошибки
    error_explicit = np.abs(u_exact - u_explicit)
    error_implicit = np.abs(u_exact - u_implicit)

    plot_solutions(x, t, u_explicit, u_implicit, u_exact[-1])

    # Построение графика с использованием функции plot_temperature_solutions для явной и неявной схем
    plot_temperature_solutions(x, t, u_explicit, u_exact, "Явная схема")
    plot_temperature_solutions(x, t, u_implicit, u_exact, "Не явная схема")

    print("Точное решение:")
    print(u_exact[-1])  # Вывод последней строки точных результатов

    print("\nЯвная разностная схема:")
    print(u_explicit[-1])  # Вывод последней строки результатов явной схемы
    print("\nУстойчива: Да" if u_explicit[-1].max() < np.inf else "Устойчива: Нет")
    # Выведите абсолютные ошибки в последний момент времени T
    print("\nАбсолютная ошибка явной разностной схемы:")
    print(error_explicit[-1])

    print("\nНеявная разностная схема:")
    print(u_implicit[-1])  # Вывод последней строки результатов неявной схемы
    print("\nУстойчива: Да" if u_implicit[-1].max() < np.inf else "Устойчива: Нет")
    print("\nАбсолютная ошибка неявной разностной схемы:")
    print(error_implicit[-1])

    print("\nСравнительная таблица явной:")
    for i in range(11):
        print(f"Точное решение: {u_exact[-1][i]} -- Явная разностная схема: {u_explicit[-1][i]} -- Абсолютная ошибка явной разностной схемы: {error_explicit[-1][i]} ")

    print("\nСравнительная таблица неявной:")
    for i in range(11):
        print(
            f"Точное решение: {u_exact[-1][i]} -- Неявная разностная схема:: {u_implicit[-1][i]} -- Абсолютная ошибка неявной разностной схемы: {error_implicit[-1][i]}")


if __name__ == '__main__':
    main()
