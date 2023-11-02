import matplotlib.pyplot as plt


# Функция для интерполяции кубическими сплайнами
def cubic_spline_interpolation(x, y):
    n = len(x) - 1  # Количество узловых точек минус один
    h = [x[i + 1] - x[i] for i in range(n)]  # Вычисляем разности между x[i+1] и x[i]

    # Расчет коэффициентов alpha, l, mu и z
    alpha = [0] + [3 * (y[i + 1] - y[i]) / h[i] - 3 * (y[i] - y[i - 1]) / h[i - 1] for i in range(1, n)]
    l, mu, z = [1], [0], [0]

    #Коэффициенты alpha, l, mu и z используются при вычислении параметров кубического сплайна в методе интерполяции кубическими сплайнами.
    #Давайте разберемся, что они представляют собой и как они используются в алгоритме:
    #alpha - Это параметры, которые вычисляются на основе разделенных разностей второго порядка между соседними узловыми точками.
    # Для внутренних узловых точек (не первой и не последней), alpha[i] вычисляется следующим образом:
    #alpha[i] = 3 * (y[i + 1] - y[i]) / h[i] - 3 * (y[i] - y[i - 1]) / h[i - 1]
    #Здесь y[i] - значение функции в узловой точке x[i], h[i] - шаг между узловыми точками x[i] и x[i + 1].
    #l: Это массив, который представляет собой диагональные элементы матрицы системы уравнений, используемой
    # для решения сплайнов. В данной реализации первый элемент l[0] всегда равен 1.
    #mu: Это массив, содержащий элементы, обратные к элементам матрицы системы уравнений.
    #z: Это массив, который используется для хранения промежуточных результатов при вычислении коэффициентов сплайна.
    #Все эти параметры используются в процессе решения системы линейных уравнений для определения коэффициентов b, c и d
    # кубического сплайна. Процесс вычисления этих параметров сложен и требует выполнения ряда математических операций
    # для обеспечения плавного и точного интерполирования функции.

    for i in range(1, n):
        # Расчет l, mu и z для каждой итерации
        l.append(2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1])
        mu.append(h[i] / l[i])
        z.append((alpha[i] - h[i - 1] * z[i - 1]) / l[i])

    # Инициализация массивов для коэффициентов сплайна
    l, z, c, b, d = l + [1], z + [0], [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)

    # Расчет коэффициентов сплайна c, b и d снизу вверх
    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    return b, c, d


# Функция для интерполяции таблицы значений
def interpolate_table(x_data, y_data, x_values):
    b, c, d = cubic_spline_interpolation(x_data, y_data)
    y_values = []

    for x in x_values:
        i = 0

        # Находим интервал, в котором находится x
        while x > x_data[i + 1]:
            i += 1

        dx = x - x_data[i]

        # Расчет значения сплайна для x на интервале [x[i], x[i+1]]
        y = y_data[i] + b[i] * dx + c[i] * dx ** 2 + d[i] * dx ** 3
        y_values.append(y)

    return y_values


# Задача 1: Графики функции и сплайна

def f(x):
    return 1 / (1 + 25 * x ** 2)


x_values = [i / 100 for i in range(-100, 101)]
y_values = [f(x) for x in x_values]

n_values = [5, 10, 20, 50]  # Разные значения n
colors = ['b', 'g', 'r', 'c']  # Разные цвета для графиков

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)

# График исходной функции
plt.plot(x_values, y_values, label='f(x)', linestyle='--')

for n, color in zip(n_values, colors):
    x_spline = [i / 100 for i in range(-100, 101, n)]
    y_spline = interpolate_table(x_values, y_values, x_spline)

    # График кубического сплайна для разных значений n
    plt.plot(x_spline, y_spline, label=f'n={n}', color=color)

plt.title('Интерполяция функции')
plt.legend()

# Задача 2: График сплайна и узловых точек

x_data = [2, 3, 5, 7]
y_data = [4, -2, 6, -3]

x_spline_table = [i / 100 for i in range(200, 501)]
y_spline_table = interpolate_table(x_data, y_data, x_spline_table)

plt.subplot(1, 2, 2)

# График кубического сплайна и узловых точек
plt.plot(x_spline_table, y_spline_table, label='Кубический сплайн')
plt.scatter(x_data, y_data, color='red', label='Узловые точки')
plt.title('Интерполяция таблицы значений')
plt.legend()

plt.show()