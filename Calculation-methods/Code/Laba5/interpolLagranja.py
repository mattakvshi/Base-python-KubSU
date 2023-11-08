import numpy as np
import matplotlib.pyplot as plt
import math

#Определим функцию f(x) = 1 / (1 + 25x^2)
def f(x):
    return 1 / (1 + 25 * x ** 2)


#Определение функций для РАНВОМЕРНО РАСПРЕДЁЛЁННЫХ узлов
#Функция будет возвращать массив значений x, равномерно распределенных на отрезке [-1, 1].
def uniform_nodes(n):
    return np.linspace(-1, 1, n)

#Определение функций для ЧЕБЫШЕВСКИХ узлов
#Функция будет возвращать массив значений x, распределенных по Чебышевским узлам на отрезке [-1, 1].
def chebyshev_nodes(n):
    return np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))


#Определение функции для вычисления интерполяционного многочлена Лагранжа
#Функция будет принимать массивы xi и yi с узлами и значениями функции в узлах, а также значение x, для которого нужно вычислить интерполяционное значение.
def lagrange_interpolation(xi, yi, x):
    n = len(xi)
    result = 0.0
    for i in range(n):
        term = yi[i]
        for j in range(n):
            if j != i:
                term *= (x - xi[j]) / (xi[i] - xi[j])
        result += term
    return result


#Определение функций для построения графиков
#Функция будет строить график функции с заданным заголовком, значениями x и y, а также подписью на графике.
def plot_function(title, x, y, label):
    plt.figure(figsize=(8, 6))
    plt.title(title, fontsize=14)
    plt.plot(x, y, label=label)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()




#Решение первой задачи - построение графиков интерполяционного полинома Лагранжа с различными значениями n и узлами

#Построение графиков с равноотстоящими узлами
def interpolate_uniform_nodes(n):
    xi = uniform_nodes(n)
    yi = f(xi)
    x = np.linspace(-1, 1, 1000)
    y = [lagrange_interpolation(xi, yi, xi_val) for xi_val in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Интерполяционный полином')
    plt.plot(x, f(x), label='Исходная функция')
    plt.scatter(xi, yi, color='red', marker='o', label='Узлы интерполяции')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(f'Интерполяция с равноотстоящими узлами (n = {n})', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()


#Построение графиков с Чебышевскими узлами
def interpolate_chebyshev_nodes(n):
    xi = chebyshev_nodes(n)
    yi = f(xi)
    x = np.linspace(-1, 1, 1000)
    y = [lagrange_interpolation(xi, yi, xi_val) for xi_val in x]

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Интерполяционный полином')
    plt.plot(x, f(x), label='Исходная функция')
    plt.scatter(xi, yi, color='red', marker='o', label='Узлы интерполяции')
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title(f'Интерполяция с Чебышевскими узлами (n = {n})', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True)
    plt.show()



#Решение второй задачи - исследование отклонения ИП от исходной функции

#Создание массива значений для аргумента x
def generate_x_values():
    return np.linspace(-1, 1, 1000)

#Вычисление значений функции f(x) и интерполяционного полинома Лагранжа для каждого значения x
def compute_function_values(x_values, n, nodes_func):
    xi = nodes_func(n)
    yi = f(xi)
    function_values = f(x_values)
    interpolation_values = [lagrange_interpolation(xi, yi, xi_val) for xi_val in x_values]
    return function_values, interpolation_values


#Построение графика отклонения ИП от исходной функции
def plot_deviation(x_values, function_values, interpolation_values, n):
    deviation = np.abs(function_values - interpolation_values)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, deviation)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('|f(x) - P(x)|', fontsize=12)
    plt.title(f'Отклонение интерполяционного полинома от исходной функции (n = {n})', fontsize=14)
    plt.grid(True)
    plt.show()


def main():
    # Задаем значения n для интерполяции
    n_values = [5, 10, 15]

    #Построение графиков интерполяционного полинома Лагранжа с различными значениями n и узлами
    #Построение графиков с равноотстоящими узлами
    for n in n_values:
        interpolate_uniform_nodes(n)

    #Построение графиков с Чебышевскими узлами
    for n in n_values:
        interpolate_chebyshev_nodes(n)

    #Исследование отклонения ИП от исходной функции
    #Создание массива значений для аргумента x
    x_values = generate_x_values()

    #Вычисление значений функции f(x) и интерполяционного полинома Лагранжа для каждого значения x
    #Вычисление значений для равноотстоящих узлов и Чебышевских узлов
    for n in n_values:
        for nodes_func, label in [(uniform_nodes, 'Равноотстоящие узлы'), (chebyshev_nodes, 'Чебышевские узлы')]:
            function_values, interpolation_values = compute_function_values(x_values, n, nodes_func)

             #Построение графика отклонения ИП от исходной функции
            plot_deviation(x_values, function_values, interpolation_values, n)


if __name__ == "__main__":
    main()