import numpy as np
import matplotlib.pyplot as plt

#определение исходных данных
x_values = np.array([2, 5, 8, 11, 14, 17])
y_values = np.array([4.8, 4.8, 12.1, 15.0, 17.4, 19.7])


#1.1. Линейная функция (y = ax + b)
def linear_func(x, a, b):
    return a * x + b

#1.2. Степенная функция (y = ax^b)
def power_func(x, a, b):
    return a * np.power(x, b)

#1.3. Показательная функция (y = ae^(bx))
def exponential_func(x, a, b):
    return a * np.exp(b * x)

#1.4. Квадратичная функция (y = ax^2 + bx + c)
def quadratic_func(x, a, b, c):
    return a * x ** 2 + b * x + c

#Для решения методом наименьших квадратов необходимо найти значения параметров a, b, c, которые
# минимизируют сумму квадратов отклонений предсказанных значений y от исходных данных y_values.
# Мы можем использовать метод numpy.linalg.lstsq для вычисления этих параметров.

def method_of_least_squares(A, y):
    # Решение системы линейных уравнений
    params, residuals, _, _ = np.linalg.lstsq(A, y, rcond=None)

    return params

#Теперь мы можем вызвать функцию method_of_least_squares для каждой модели с исходными
# данными x_values и y_values, чтобы получить значения параметров.

linear_A = np.vstack([x_values, np.ones(len(x_values))]).T
linear_params = method_of_least_squares(linear_A, y_values)

power_A = np.vstack([np.log(x_values), np.ones(len(x_values))]).T
power_params = method_of_least_squares(power_A, np.log(y_values))

exponential_A = np.vstack([x_values, np.ones(len(x_values))]).T
exponential_params = method_of_least_squares(exponential_A, np.log(y_values))

quadratic_params = method_of_least_squares(np.column_stack([x_values**2, x_values, np.ones(len(x_values))]), y_values)

#Теперь у нас есть значения параметров для каждой модели. Мы можем использовать эти параметры
# для генерации предсказанных значений и построения графиков.

# Генерация значений для построения графиков
x_range = np.linspace(np.min(x_values), np.max(x_values), 100)
linear_y_pred = linear_func(x_range, *linear_params)
power_y_pred = power_func(x_range, *power_params)
exponential_y_pred = exponential_func(x_range, *exponential_params)
quadratic_y_pred = quadratic_func(x_range, *quadratic_params)

# Построение графиков
plt.scatter(x_values, y_values, label='Экспериментальные точки')
plt.plot(x_range, linear_y_pred, label='Линейная функция')
plt.plot(x_range, power_y_pred, label='Степенная функция')
plt.plot(x_range, exponential_y_pred, label='Показательная функция')
plt.plot(x_range, quadratic_y_pred, label='Квадратичная функция')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Аппроксимация методом наименьших квадратов')
plt.show()

if __name__ == '__main__':
    print('Исходные данные:')
    print('x_values:', x_values)
    print('y_values:', y_values)
    print()

    print('Аппроксимирующая функция - Линейная:')
    print('y = {:.2f} * x + {:.2f}'.format(*linear_params))
    print()

    print('Аппроксимирующая функция - Степенная:')
    print('y = {:.2f} * x^{:.2f}'.format(np.exp(power_params[1]), power_params[0]))
    print()

    print('Аппроксимирующая функция - Показательная:')
    print('y = {:.2f} * exp({:.2f} * x)'.format(np.exp(exponential_params[1]), exponential_params[0]))
    print()

    print('Аппроксимирующая функция - Квадратичная:')
    print('y = {:.2f} * x^2 + {:.2f} * x + {:.2f}'.format(*quadratic_params))
    print()