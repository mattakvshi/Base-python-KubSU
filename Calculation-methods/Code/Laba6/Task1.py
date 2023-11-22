import random
import math
import matplotlib.pyplot as plt


def calculate_area_triangle(n, N):
    # Шаг 1: Построить графики функций y = f1(x) и y = f2(x)
    x = [i / N * n for i in range(N + 1)]
    f1 = [10 * xi / n for xi in x]
    f2 = [(10 * (xi - 20) / (n - 20) + 20) for xi in x]

    # Шаг 2: Выбрать размеры прямоугольника, который содержит фигуру
    a = max(f2)
    b = min(f1)

    # Шаг 3: Генерация случайных точек в прямоугольнике
    points = []
    for _ in range(N):
        xi = random.uniform(0, n)
        yi = random.uniform(b, a)
        points.append((xi, yi))

    # Шаг 4: Проверка точек на принадлежность фигуре
    M = sum(1 for xi, yi in points if f1[int(xi / n * N)] < yi < f2[int(xi / n * N)])

    # Шаг 5: Вычисление приближенной площади фигуры
    area = ((n * (a - b)) * M) / (N * (n - 20))

    # Шаг 6: Оценка погрешности метода Монте-Карло
    absolute_error = abs(area - (n * (a - b)))
    relative_error = absolute_error / (n * (a - b))

    return area, absolute_error, relative_error


# Пример использования функции calculate_area_triangle
n = 20  # Размер фигуры
N = 100  # Количество точек

area, absolute_error, relative_error = calculate_area_triangle(n, N)

print("Задание 1:")
print("==========")
print(f"Приближенная площадь треугольника: {area}")
print(f"Абсолютная погрешность: {absolute_error}")
print(f"Относительная погрешность: {relative_error}")
