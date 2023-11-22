import random
import math
import matplotlib.pyplot as plt


def calculate_area_polar(n, N):
    # Шаг 1: Построение графика фигуры в декартовых координатах
    points = []
    for _ in range(N):
        phi = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, n)

        x = r * math.cos(phi)
        y = r * math.sin(phi)

        points.append((x, y))

    # Шаг 2: Вычисление количества точек, попавших внутрь фигуры
    M = sum(1 for x, y in points if n + 10 * math.sin(x) ** 2 + (n - 10) * math.cos(x) ** 2 > y ** 2)

    # Шаг 3: Вычисление приближенной площади фигуры
    area = (4 * math.pi * n ** 2 * M) / N

    return area


# Пример использования функции calculate_area_polar
n = 5  # Радиус фигуры
N = 1000  # Количество точек

area = calculate_area_polar(n, N)

print("Задание 4:")
print("==========")
print(f"Приближенная площадь фигуры: {area}")
