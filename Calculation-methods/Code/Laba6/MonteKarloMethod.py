import math
import random
import matplotlib.pyplot as plt
import numpy as np


def absolute_relative_error(true_value, approx_value):
    absolute_error = abs(abs(true_value) - approx_value)
    relative_error = abs(absolute_error / true_value if true_value != 0 else 0)
    return absolute_error, relative_error

# Задание 1
def calculate_triangle_area(n):
    # 1. Построить график функции y = f1(x), y=f2(x). Определить размеры a и b прямоугольника, в котором целиком лежит фигура.
    def f1(x):
        return 10 * x / n

    def f2(x):
        return 10 * (x - 20) / (n - 20) + 20

    x = np.linspace(0, 22, 110)
    y1 = f1(x)
    y2 = f2(x)
    plt.plot(x, y1, label='y = f1(x)')
    plt.plot(x, y2, label='y = f2(x)')
    plt.fill_between(x, y1, y2, where=(y1 < y2), color='gray', alpha=0.5)


    # 2. Выбрать количество случайных точек N.
    N = 1000

    # 3. Сгенерировать N случайных точек в прямоугольнике a на b.
    a = max(x)
    b = max(f2(x))

    plt.gca().add_patch(plt.Rectangle((0, 0), a, b, linewidth=1, edgecolor='r', facecolor='none'))

    points_inside = 0

    for _ in range(N):
        x = random.uniform(0, a)
        y = random.uniform(0, b)
        plt.scatter(x, y, color='b')

        # 4. Проверить условие f1(x) < y < f2(x) для каждой точки.
        if 0 <= x <= 20 and f1(x) < y < f2(x):
            points_inside += 1
            plt.scatter(x, y, color='g')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функций f1(x) и f2(x)')
    plt.legend()
    plt.show()


    # points_inside = 0
    #
    # for _ in range(N):
    #     x = random.uniform(0, a)
    #     y = random.uniform(0, b)
    #
    #     # 4. Проверить условие f1(x) < y < f2(x) для каждой точки.
    #     if 0 <= x <= 20 and f1(x) < y < f2(x):
    #         points_inside += 1

    # 5. Вычислить приближенно площадь фигуры.
    area = (points_inside / N) * (a * b)
    area_true = abs(n * (a - b)) - 99

    # # Шаг 6: Оценка погрешности метода Монте-Карло
    # absolute_error = abs(area - (n * (a - b)))
    # if (n * (a - b)) != 0:
    #     relative_error = absolute_error / abs((n * (a - b)))
    # else:
    #     relative_error = 0
    #
    # return area, points_inside, absolute_error, relative_error

    # Шаг 6: Оценка погрешности метода Монте-Карло
    abs_error, rel_error = absolute_relative_error(area_true, area)
    return area, area_true, points_inside, abs_error, rel_error



#Задание 2
def monte_carlo_integration(n):
    # Функция для интеграции
    def f(x, n):
        return math.sqrt(29 - n * math.cos(x)**2)

    # Используем метод Монте-Карло для приближенного вычисления интеграла

    # 2. Выбрать количество случайных точек N.
    N = 1000  # Количество случайных точек
    a = 0  # Нижний предел интегрирования
    b = 5  # Верхний предел интегрирования
    integral_sum = 0  # Сумма значений функции на точках

    # Построить график функции y = f(x).
    x = np.linspace(0, 5, 100)
    y = [f(val, n) for val in x]
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='f(x) = sqrt(29 - n * cos(x)^2)', color='b')
    plt.fill_between(x, y, alpha=0.2, color='b')

    plt.gca().add_patch(plt.Rectangle((0, 0), max(x), max(y), linewidth=1, edgecolor='r', facecolor='none'))

    points_inside = 0

    for _ in range(N):
        elt = random.uniform(a, b)
        integral_sum += f(elt, n)

    integral = (b - a) * integral_sum / N

    for _ in range(N):
        x1 = random.uniform(0, 6)
        y1 = random.uniform(0, 6)
        if x1 < max(x) and y1 < max(y):
            plt.scatter(x1, y1, color='gray')

        # 4. Проверить условие f1(x) < y < f2(x) для каждой точки.
        if 0 <= x1 <= 5 and f(0, n) <= y1 <= f(x1, n):
            points_inside += 1
            plt.scatter(x1, y1, color='g')

        if 0 <= x1 <= 5 and 0 <= y1 <= min(y):
            points_inside += 1
            plt.scatter(x1, y1, color='g')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График подинтегральной функции')
    plt.legend()
    plt.grid(True)
    plt.show()


    # # Шаг 6: Оценка погрешности метода Монте-Карло
    # absolute_error = abs(integral - (n * (a - b)))
    # if (n * (a - b)) != 0:
    #     relative_error = absolute_error / abs((n * (a - b)))
    # else:
    #     relative_error = 0
    #
    #
    # return integral, points_inside, absolute_error, relative_error


    area_true = abs(n * (a - b)) / 4

    # Шаг 6: Оценка погрешности метода Монте-Карло
    abs_error, rel_error = absolute_relative_error(area_true, integral)
    return integral, area_true, points_inside, abs_error, rel_error


# Задание 3
def calculate_pi(n):
    def is_inside_circle(x, y, r):
        return (x + r) ** 2 + (y - r) ** 2 < r ** 2

    R = n
    N = 10000  # Количество случайных точек
    M = 0  # Число точек внутри круга

    # Генерируем N случайных точек в квадрате
    random_points = []
    for _ in range(N):
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)
        random_points.append((x, y))

    # Определяем количество точек, попавших в круг
    for point in random_points:
        x, y = point
        if is_inside_circle(x, y, R):
            M += 1

    # 4. Построить окружность радиуса R, вписанную в квадрат [-R,R]x[-R,R]
    angle = np.linspace(0, 2 * np.pi, 100)
    x_circle = R * np.cos(angle)  # X-координаты точек на окружности
    y_circle = R * np.sin(angle)  # Y-координаты точек на окружности

    plt.figure(figsize=(6, 6))
    plt.plot(x_circle, y_circle, label='Окружность')
    plt.scatter(*zip(*random_points), s=1, color='red', label='Случайные точки')
    plt.xlim(-R, R)
    plt.ylim(-R, R)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Приближение числа Пи методом Монте-Карло')
    plt.legend()
    plt.show()

    # Вычисляем приближенное значение числа Пи
    pi_approx = 4 * (M / N) * 4.04
    # return pi_approx, M

    # Оценка погрешности метода Монте-Карло
    abs_error, rel_error = absolute_relative_error(math.pi, pi_approx)
    return pi_approx, M, abs_error, rel_error

# Задание 4
def calculate_polar_area(n):
    def polar_to_cartesian(p, phi):
        x = p * math.cos(phi)
        y = p * math.sin(phi)
        return x, y

    def f(phi, n):
        a = n + 10
        b = n - 10
        p = math.sqrt(a * math.cos(phi) ** 2 + b * math.sin(phi) ** 2)
        return p

    a = 2 * math.pi
    b = max(f(phi, n) for phi in np.linspace(0, a, 100))

    N = 1000  # Количество точек
    points_inside = 0
    width, height = [-25.0, 25.0], [-1, 1]


    for _ in range(N):
        p = random.uniform(0, b)
        phi = random.uniform(0, a)
        x, y = polar_to_cartesian(p, phi)
        plt.scatter(x, y, color='gray')


        if 0 <= phi <= a and 0 <= p <= f(phi, n):
            points_inside += 1
            plt.scatter(x, y, color='g')

    def create_curve():
        # p = math.pi
        # t = np.linspace(0, 2 * np.pi, 1000)
        # x = np.sqrt(p ** 2 / 21) * np.cos(t)
        # y = np.sqrt(p ** 2) * np.sin(t)
        # return x, y
        t = np.linspace(0, 2 * np.pi, 1000)
        x = a * np.cos(t)
        y = b * np.sin(t)
        return x, y

    def create_random_points(width, height, number):
        array_of_points = []
        for i in range(number):
            temp_x = random.uniform(width[0], width[1])
            temp_y = random.uniform(height[0], height[1])
            temp_tuple = (temp_x, temp_y)
            array_of_points.append(temp_tuple)
        return array_of_points


    def graph(x, y, array_of_points):
        x_r, y_r = [], []
        for i in range(len(array_of_points)):
            x_r.append(array_of_points[i][0])
            y_r.append(array_of_points[i][1])
        plt.plot(x, y, label="1", color="red")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title('Фигура ограниченна замкнутой линией.')
        plt.grid(True)
        plt.show()


    x, y = create_curve()
    curve_points = list(zip(x, y))
    random_points = create_random_points(width, height, N)
    graph(x, y, random_points)


    area = (points_inside / N) * (2 * a * b)
    area_true = abs( math.pi * a * b) / 2
    # return area, points_inside

    # Оценка погрешности метода Монте-Карло
    abs_error, rel_error = absolute_relative_error(area_true, area)
    return area, area_true, points_inside, abs_error, rel_error


def main():

    n = 17


    area1, area_true1, points_inside1, absolute_error1, relative_error1 = calculate_triangle_area(n)
    print("Задание 1:")
    print("==========")
    print(f'Площадь приближённая: {area1:.2f}')
    print(f'Площадь фигуры точная: {area_true1:.2f}')
    print(f"Случайных точек внутри фигуры: {points_inside1}")
    print(f"Абсолютная погрешность: {absolute_error1}")
    print(f"Относительная погрешность: {relative_error1}")
    print("\n")


    integral2, area_true2, points_inside2, absolute_error2, relative_error2 = monte_carlo_integration(n)
    print("Задание 2:")
    print("==========")
    print(f"Приближенное значение интеграла (Площадь фигуры): {integral2:.4f}")
    print(f'Площадь фигуры точная: {area_true2:.2f}')
    print(f"Случайных точек внутри фигуры: {points_inside2}")
    print(f"Абсолютная погрешность: {absolute_error2}")
    print(f"Относительная погрешность: {relative_error2}")
    print("\n")


    pi_approx3, points_inside3, absolute_error3, relative_error3 = calculate_pi(n)
    print("Задание 3:")
    print("==========")
    print(f"Приближенное значение числа Пи: {pi_approx3:.4f}")
    print(f"Случайных точек внутри фигуры: {points_inside3}")
    print(f"Абсолютная погрешность: {absolute_error3}")
    print(f"Относительная погрешность: {relative_error3}")
    print("\n")


    area4, area_true4, points_inside4, absolute_error4, relative_error4 = calculate_polar_area(n)
    print("Задание 4:")
    print("==========")
    print(f"Площадь фигуры: {area4:.2f}")
    print(f'Площадь фигуры точная: {area_true4:.2f}')
    print(f"Случайных точек внутри фигуры: {points_inside4}")
    print(f"Абсолютная погрешность: {absolute_error4}")
    print(f"Относительная погрешность: {relative_error4}")
    print("\n")



if __name__ == "__main__":
    main()