import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
import time

# ----- Функция для вычисления функции ошибок (erf) -----

# Исходная функция под интегралом для erf
f_erf = lambda t: np.exp(-t ** 2)

def my_erf(x, n=1000):
    """
    Вычисляет функцию ошибок (erf) методом прямоугольников.

    :param x: Верхняя граница интегрирования
    :param n: Количество делений интервала (точность)
    :return: Значение erf(x)
    """
    h = x / n
    res = 0

    for i in range(n):
        res += f_erf(i * h)

    res *= 2 / math.sqrt(math.pi) * h

    return res

# ----- Приближенное вычисление Пи -----

# Исходная функция под интегралом для Пи
f_pi = lambda x: 4 / (1 + x * x)

def trap_pi(n=1000):
    """
    Вычисляет приближенное значение числа Пи методом трапеций.

    :param n: Количество делений интервала
    :return: Приближенное значение числа Пи
    """
    h = 1 / n
    res = 0.5 * (f_pi(0) + f_pi(1))
    for i in range(1, n):
        res += f_pi(i * h)
    return res * h

def rect_pi(n=1000):
    """
    Вычисляет приближенное значение числа Пи методом прямоугольников.

    :param n: Количество делений интервала
    :return: Приближенное значение числа Пи
    """
    h = 1 / n
    res = 0
    for i in range(n):
        res += f_pi((i + 0.5) * h)
    return res * h

def spline_pi(n=1000):
    """
    Вычисляет приближенное значение числа Пи с использованием сплайн-интерполяции.

    :param n: Количество делений интервала
    :return: Приближенное значение числа Пи
    """
    x = np.linspace(0, 1, n)
    cs = CubicSpline(x, f_pi(x))
    return cs.integrate(0, 1)

# ----- Вычисление интеграла сложной функции -----

# Сложная функция для интегрирования
f_complex = lambda x: np.where(x <= 2, np.exp(x*x), 1/(4 - np.sin(16*np.pi*x)))

def integrate_complex(f, a, b, n=10000000):
    """
    Вычисляет определенный интеграл от непрерывной функции на заданном интервале.

    :param f: Интегрируемая функция
    :param a: Нижний предел интегрирования
    :param b: Верхний предел интегрирования
    :param n: Количество делений интервала
    :return: Значение определенного интеграла
    """
    x = np.linspace(a, b, n)
    cs = CubicSpline(x, f(x))
    return cs.integrate(a, b)


# Функция для построения графика функции ошибок (erf)
def plot_erf():
    x_values = np.linspace(0, 2, 21)
    erf_values = [my_erf(x) for x in x_values]
    true_erf_values = [math.erf(x) for x in x_values]

    plt.figure(figsize=(15, 5))

    # Создаем сетку для 3 графиков: 1 ряд, 3 колонки
    plt.subplot(1, 3, 1)
    plt.plot(x_values, erf_values, 'o-', color='orange', label='Метод прямоугольников')
    plt.plot(x_values, true_erf_values, 's-', color='purple', alpha=0.5, label='Точное значение')
    plt.title('График функции ошибок erf(x)')
    plt.xlabel('x')
    plt.ylabel('erf(x)')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 3, 2)
    plt.plot(x_values, true_erf_values, 's-', color='purple', label='Точное значение')
    plt.title('График точного значения erf(x)')
    plt.xlabel('x')
    plt.ylabel('erf(x)')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 3, 3)
    plt.plot(x_values, erf_values, 'o-', color='orange', label='Метод прямоугольников')
    plt.title('График метода прямоугольников')
    plt.xlabel('x')
    plt.ylabel('erf(x)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()  # Для того чтобы графики не сливались
    plt.show()


# Функция для построения графиков приближения числа Пи
def plot_pi_approximation():
    n_values = [8, 32, 128]
    pi_values = []

    for n in n_values:
        trap = trap_pi(n)
        rect = rect_pi(n)
        spline = spline_pi(n)
        pi_values.append((trap, rect, spline))

    fig, ax = plt.subplots(figsize=(10, 5))

    for i, n in enumerate(n_values):
        ax.plot(['Трапеции', 'Прямоугольники', 'Сплайны'], pi_values[i], 'o-', label=f'n = {n}')

    ax.axhline(math.pi, color='gray', linewidth=2, label='Точное значение Пи')
    ax.set_title('Приближенные значения числа Пи разными методами')
    ax.set_ylabel('Значение Пи')
    ax.legend()
    ax.grid(True)
    plt.show()


# ----- (main) -----

def main():
    # Вывод таблицы значений функции ошибок (erf)
    print("\n\n__________________ ЗАДАНИЕ 1 __________________")
    print("Таблица значений функции ошибок (erf):")

    start_time = time.time() # время до создания таблицы

    for i in range(21):
        calculated_erf = my_erf(i * 0.1)
        true_erf = math.erf(i * 0.1)
        print(f"x = {i * 0.1:.1f}, Метод прямоугольников: {calculated_erf:.5f}, Точное значение: {true_erf:.5f}")

    end_time = time.time()  # время после создания таблицы
    duration = end_time - start_time  # сколько  это заняло

    print(f"\nГенерация таблицы ошибок заняла {duration:.4f} секунд(ы).")

    # Вывод результатов приближенного вычисления Пи
    print("\n\n__________________ ЗАДАНИЕ 2 __________________")
    print("\nПриближенные значения числа Пи:")
    for n in [8, 32, 128]:
        print(f"\nn = {n}")
        t1 = trap_pi(n)
        t2 = rect_pi(n)
        t3 = spline_pi(n)
        print(f"Метод трапеций: {t1:.6f}, Абсолютная ошибка: {abs(math.pi - t1):.6f}")
        print(f"Метод прямоугольников: {t2:.6f}, Абсолютная ошибка: {abs(math.pi - t2):.6f}")
        print(f"Сплайн-квадратуры: {t3:.15f}, Абсолютная ошибка: {abs(math.pi - t3):.15f}")

    # Вывод результатов вычисления интеграла сложной функции
    print("\n\n__________________ ЗАДАНИЕ 3 __________________")
    print("\nВычисление интеграла сложной функции на интервале [0, 4]:")
    direct_integral, _ = quad(f_complex, 0, 4, limit=100)
    spline_integral = integrate_complex(f_complex, 0, 4)
    print(f"Прямое вычисление: {direct_integral}, Сплайн-интерполяция: {spline_integral},")
    print(f"Абсолютная ошибка сплайн-интерполяции: {abs(direct_integral-spline_integral)}")

if __name__ == "__main__":
    main()
    plot_erf()
    plot_pi_approximation()
