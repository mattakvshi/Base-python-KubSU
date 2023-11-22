import random
import math
import matplotlib.pyplot as plt


def estimate_pi(n, N):
    # Шаг 1: Вычисление количества точек, попавших внутрь круга S
    points = []
    for _ in range(N):
        xi = random.uniform(-n, n)
        yi = random.uniform(-n, n)
        points.append((xi, yi))

    M = sum(1 for xi, yi in points if (xi + n) ** 2 + (yi - n) ** 2 < n ** 2)

    # Шаг 2: Вычисление приближенного значения числа Pi
    pi_approx = 4 * (M / N)

    return pi_approx


# Пример использования функции estimate_pi
n = 1  # Радиус круга
N = 1000  # Количество точек

pi_approx = estimate_pi(n, N)

print("Задание 3:")
print("==========")
print(f"Приближенное значение числа Pi: {pi_approx}")
