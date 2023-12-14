import numpy as np
import matplotlib.pyplot as plt
import math
import time

#ЭЙЛЕР
# def error_function():
#     start_time = time.time()  # Начало замера времени
#
#     erf_func = lambda x: (2 / np.sqrt(np.pi)) * np.exp(-x ** 2)
#
#     x_vals_erf = np.linspace(0, 2, 21)  # Генерация значений x от 0 до 2 с шагом 0.1
#     y_vals_erf = []
#
#     # Расчет значения функции ошибок вручную методом Эйлера
#     N = 1000
#     x_end = 2
#     h = x_end / N
#
#     def euler_method(func, x0, y0, x_end, N):
#         y = y0
#         for i in range(int(x_end / h)):
#             y += h * func(i * h)
#         return y
#
#     # Таблица значений функции ошибок
#     print("Таблица значений функции ошибок:")
#     for x in x_vals_erf:
#         y = euler_method(erf_func, 0, 0, x, N)
#         y_vals_erf.append(y)
#         print(f"erf({x:.1f}) = {y}")
#
#     generation_time = time.time() - start_time  # Фиксация затраченного времени
#     print(f"\nВремя генерации таблицы: {generation_time:.4f} секунд\n")
#
#     # Отображаем график
#     plt.plot(x_vals_erf, y_vals_erf)
#     plt.xlabel('x')
#     plt.ylabel('erf(x)')
#     plt.title('График функции ошибок (Метод Эйлера)')
#     plt.show()




#РУНГЕ-КУТТА
def runge_kutta_method(func, x0, y0, x_end, N):
    h = (x_end - x0) / N
    y = y0
    x = x0
    for i in range(N):
        k1 = h * func(x)
        k2 = h * func(x + 0.5 * h)
        k3 = h * func(x + 0.5 * h)
        k4 = h * func(x + h)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
    return y

def error_function():
    start_time = time.time()

    erf_func = lambda x: (2 / np.sqrt(np.pi)) * np.exp(-x ** 2)

    x_vals_erf = np.linspace(0, 2, 21)
    y_vals_erf = []

    N = 1000
    x_end = 2

    print("Таблица значений функции ошибок:")
    for x in x_vals_erf:
        y = runge_kutta_method(erf_func, 0, 0, x, N)
        y_vals_erf.append(y)
        print(f"erf({x:.1f}) = {y}")

    generation_time = time.time() - start_time
    print(f"\nВремя генерации таблицы: {generation_time:.4f} секунд\n")

    plt.plot(x_vals_erf, y_vals_erf)
    plt.xlabel('x')
    plt.ylabel('erf(x)')
    plt.title('График функции ошибок (Метод Рунге-Кутты)')
    plt.show()


def rabbit_and_fox(r0, f0):
    a = 0.01  # Коэффициент взаимодействия
    b = 0.1  # Коэффициент умирания кроликов
    c = 0.1  # Коэффициент умирания лис
    t_end = 100  # Время моделирования
    N = 10000  # Количество шагов
    h = t_end / N  # Шаг

    rab_growth = lambda r, f: 2 * r - a * r * f - b * r
    fox_growth = lambda r, f: -f + a * r * f - c * f

    r_values = np.zeros(N + 1)
    f_values = np.zeros(N + 1)
    r_values[0], f_values[0] = r0, f0

    for i in range(N):
        r_values[i + 1] = r_values[i] + h * rab_growth(r_values[i], f_values[i])
        f_values[i + 1] = f_values[i] + h * fox_growth(r_values[i], f_values[i])

    print(f"С начальными условиями r_0 = {r0}, f_0 = {f0}, после {t_end} единиц времени, имеем:")
    print(f"Количество кроликов: {r_values[-1]}")
    print(f"Количество лис: {f_values[-1]}\n")

    if r_values[-1] < 1:
        print("Кролики вымирают.\n")
    if f_values[-1] < 1:
        print("Лисы вымирают.\n")

    # Визуализация результатов
    t_values = np.linspace(0, t_end, N + 1)
    plt.plot(t_values, r_values, label='Кролики')
    plt.plot(t_values, f_values, label='Лисы')
    plt.xlabel('Время t')
    plt.ylabel('Популяция')
    plt.legend()
    plt.title(f'Динамика популяции кроликов и лис (r_0={r0}, f_0={f0})')
    plt.show()

    return r_values, f_values


def main():
    print("1. Моделирование функции ошибок:")
    error_function()

    print("\n2. Моделирование динамики популяций:")
    rabbit_and_fox(15, 22)  # Кастомные начальные значения для демонстрации исчезновения кроликов

    # Теперь найдем условия, при которых лисы исчезнут.
    # Перебор начальных условий и поиск случая, когда популяция лис падает ниже 1.
    print("\nПоиск начальных условий, при которых вымирают лисы:")
    for initial_population in range(5, 26):
        r_values, f_values = rabbit_and_fox(initial_population, initial_population)
        if f_values[-1] < 1:
            print(f"Лисы вымирают, если r_0 = f_0 = {initial_population}\n")
            break


if __name__ == "__main__":
    main()

