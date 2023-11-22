import random
import math


def monte_carlo_integration(func, a, b, n):
    # Шаг 1: Генерация случайных точек в прямоугольнике
    points = []
    for _ in range(n):
        xi = random.uniform(a, b)
        yi = random.uniform(0, 1)
        points.append((xi, yi))

    # Шаг 2: Вычисление приближенного значения интеграла
    total = sum(func(xi) for xi, _ in points)
    integral = (b - a) * total / n

    return integral


# Пример использования функции monte_carlo_integration
def func(x):
    return math.sqrt(29 - n * math.cos(x) ** 2)


n = 29  # Некоторое значение для n
a = 0  # Нижний предел интегрирования
b = 5  # Верхний предел интегрирования
N = 1000  # Количество точек

integral = monte_carlo_integration(func, a, b, N)

print("Задание 2:")
print("==========")
print(f"Приближенное значение интеграла: {integral}")
