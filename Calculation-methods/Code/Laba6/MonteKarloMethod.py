import math
import random
import matplotlib.pyplot as plt
import numpy as np

# Задание 1
def calculate_triangle_area(n):
    # 1. Построить график функции y = f1(x), y=f2(x). Определить размеры a и b прямоугольника, в котором целиком лежит фигура.
    def f1(x):
        return 10 * x / n

    def f2(x):
        return 10 * (x - 20) / (n - 20) + 20

    x = np.linspace(0, 20, 100)
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

    # Шаг 6: Оценка погрешности метода Монте-Карло
    absolute_error = abs(area - (n * (a - b)))
    if (n * (a - b)) != 0:
        relative_error = absolute_error / abs((n * (a - b)))
    else:
        relative_error = 0

    return area, points_inside, absolute_error, relative_error



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


    # Шаг 6: Оценка погрешности метода Монте-Карло
    absolute_error = abs(integral - (n * (a - b)))
    if (n * (a - b)) != 0:
        relative_error = absolute_error / abs((n * (a - b)))
    else:
        relative_error = 0


    return integral, points_inside, absolute_error, relative_error


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
    return pi_approx, M


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


    for _ in range(N):
        p = random.uniform(0, b)
        phi = random.uniform(0, a)
        x, y = polar_to_cartesian(p, phi)
        plt.scatter(x, y, color='gray')


        if 0 <= phi <= a and 0 <= p <= f(phi, n):
            points_inside += 1
            plt.scatter(x, y, color='g')


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Фигура ограниченна замкнутой линией.')
    plt.legend()
    plt.show()


    area = (points_inside / N) * (2 * a * b)
    return area, points_inside



def main():

    n = 17


    area1, points_inside1, absolute_error1, relative_error1 = calculate_triangle_area(n)
    print("Задание 1:")
    print("==========")
    print(f'Площадь фигуры: {area1:.2f}')
    print(f"Случайных точек внутри фигуры: {points_inside1}")
    print(f"Абсолютная погрешность: {absolute_error1}")
    print(f"Относительная погрешность: {relative_error1}")
    print("\n")


    integral2, points_inside2, absolute_error2, relative_error2 = monte_carlo_integration(n)
    print("Задание 2:")
    print("==========")
    print(f"Приближенное значение интеграла (Площадь фигуры): {integral2:.4f}")
    print(f"Случайных точек внутри фигуры: {points_inside2}")
    print(f"Абсолютная погрешность: {absolute_error2}")
    print(f"Относительная погрешность: {relative_error2}")
    print("\n")


    pi_approx3, points_inside3 = calculate_pi(n)
    print("Задание 3:")
    print("==========")
    print(f"Приближенное значение числа Пи: {pi_approx3:.4f}")
    print(f"Случайных точек внутри фигуры: {points_inside3}")
    print("\n")


    area4, points_inside4 = calculate_polar_area(n)
    print("Задание 4:")
    print("==========")
    print(f"Площадь фигуры: {area4:.2f}")
    print(f"Случайных точек внутри фигуры: {points_inside4}")
    print("\n")



if __name__ == "__main__":
    main()