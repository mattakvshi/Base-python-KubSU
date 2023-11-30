import matplotlib.pyplot as plt
import random
import math

def f1(x, n):
    return 10 * x / n

def f2(x, n):
    return 10 * (x - 20) / (n - 20) + 20

def plot_functions(n):
    x = list(range(0, n + 1))
    y1 = [f1(xi, n) for xi in x]
    y2 = [f2(xi, n) for xi in x]

    plt.plot(x, y1, label='f1(x)')
    plt.plot(x, y2, label='f2(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphs of f1(x) and f2(x)')
    plt.legend()
    plt.show()

def monte_carlo_triangle_area(n, N):
    a, b = 0, n
    M = 0

    for _ in range(N):
        xi = random.uniform(a, b)
        yi = random.uniform(0, max(f1(xi, n), f2(xi, n)))

        if f1(xi, n) < yi < f2(xi, n):
            M += 1

    S_approx = (M / N) * (b - a) * max(f2(b, n), f2(a, n))
    return S_approx

def absolute_relative_error(true_value, approx_value):
    absolute_error = abs(true_value - approx_value)
    relative_error = absolute_error / true_value if true_value != 0 else 0
    return absolute_error, relative_error

def task1(n, N):
    print("Задание 1:")
    plot_functions(n)

    a, b = 0, n
    true_area = (b - a) * max(f2(b, n), f2(a, n))

    S_approx = monte_carlo_triangle_area(n, N)

    abs_error, rel_error = absolute_relative_error(true_area, S_approx)

    print(f"Площадь фигуры (истинное значение): {true_area}")
    print(f"Площадь фигуры (приближенное значение): {S_approx}")
    print(f"Абсолютная погрешность: {abs_error}")
    print(f"Относительная погрешность: {rel_error}\n")

def monte_carlo_integral(n, N):
    a, b = 0, 5
    M = 0

    for _ in range(N):
        xi = random.uniform(a, b)
        yi = random.uniform(0, math.sqrt(29 - n * math.cos(xi)**2))

        if yi > 0:
            M += 1

    S_approx = (M / N) * (b - a) * math.sqrt(29 - n * 0**2)
    return S_approx

def task2(n, N):
    print("Задание 2:")
    S_approx = monte_carlo_integral(n, N)

    abs_error, rel_error = absolute_relative_error(29 * (5 - 0), S_approx)

    print(f"Интеграл (истинное значение): {29 * (5 - 0)}")
    print(f"Интеграл (приближенное значение): {S_approx}")
    print(f"Абсолютная погрешность: {abs_error}")
    print(f"Относительная погрешность: {rel_error}\n")

def monte_carlo_pi(n, N):
    R = n
    M = 0

    for _ in range(N):
        xi = random.uniform(-R, R)
        yi = random.uniform(-R, R)

        if xi**2 + yi**2 < R**2:
            M += 1

    pi_approx = 4 * (M / N)
    return pi_approx

def task3(n, N):
    print("Задание 3:")
    pi_approx = monte_carlo_pi(n, N)

    abs_error, rel_error = absolute_relative_error(math.pi, pi_approx)

    print(f"Число Pi (истинное значение): {math.pi}")
    print(f"Число Pi (приближенное значение): {pi_approx}")
    print(f"Абсолютная погрешность: {abs_error}")
    print(f"Относительная погрешность: {rel_error}\n")

def polar_to_cartesian(p, phi):
    x = p * math.cos(phi)
    y = p * math.sin(phi)
    return x, y

def f_polar(phi, n):
    A = n + 10
    B = n - 10
    return A * math.cos(phi)**2 + B * math.sin(phi)**2

def monte_carlo_polar_area(n, N):
    a, b = 0, 2 * math.pi
    M = 0

    for _ in range(N):
        phi = random.uniform(a, b)
        ri = random.uniform(0, f_polar(b, n))

        if ri < f_polar(phi, n):
            M += 1

    S_approx = (M / N) * (b - a) * f_polar(b, n)
    return S_approx

def task4(n, N):
    print("Задание 4:")
    a, b = 0, 2 * math.pi
    r = max(f_polar(b, n))

    true_area = (b - a) * r

    S_approx = monte_carlo_polar_area(n, N)

    abs_error, rel_error = absolute_relative_error(true_area, S_approx)

    print(f"Площадь фигуры (истинное значение): {true_area}")
    print(f"Площадь фигуры (приближенное значение): {S_approx}")
    print(f"Абсолютная погрешность: {abs_error}")
    print(f"Относительная погрешность: {rel_error}\n")

if __name__ == "__main__":
    n = 17
    N = 100

    task1(n, N)
    task2(n, N)
    task3(n, N)
    task4(n, N)
