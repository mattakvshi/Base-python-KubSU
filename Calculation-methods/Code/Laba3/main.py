import numpy as np
from scipy.special import erf

# Определение функции ошибок
def my_erf(x):
    return 2/np.sqrt(np.pi) * np.exp(-x**2)

def task1():
    # Матрица коэффициентов
    A = np.array([[1.00, 0.80, 0.64],
                  [1.00, 0.90, 0.81],
                  [1.00, 1.10, 1.21]])

    # Вектор свободных членов
    b = np.array([my_erf(0.80), my_erf(0.90), my_erf(1.10)])
    b1 = np.array([erf(0.80), erf(0.90), erf(1.10)])

    # Решение системы
    x = np.linalg.solve(A, b)
    x1 = np.linalg.solve(A, b1)


    print("Через my_erf: ")
    # Вывод результата
    print("Решение X1, X2, X3:")
    print(x)
    print("\n")

    # Сумма решений
    sum_x = np.sum(x)
    print("Сумма решений X1 + X2 + X3:")
    print(sum_x)
    print("\n")


    print("Через erf: ")
    # Вывод результата
    print("Решение X1, X2, X3:")
    print(x1)
    print("\n")

    # Сумма решений
    sum_x = np.sum(x1)
    print("Сумма решений X1 + X2 + X3:")
    print(sum_x)
    print("\n")

    # Значение erf(1.0)
    erf_1 = erf(1.0)
    print("Значение erf(1.0):")
    print(erf_1)
    print("\n")



# Теорема Руше о рангах
#
# Если ранг основной матрицы совпадает с рангом расширенной матрицы и равен числу переменных, то система имеет
# единственное решение. Если ранги совпадают, но меньше числа переменных, то система имеет бесконечное число решений.
# Если ранги не совпадают, то система несовместна, то есть не имеет решений.
def task2():
    # Матрица коэффициентов
    A = np.array([[0.1, 0.2, 0.3],
                  [0.4, 0.5, 0.6],
                  [0.7, 0.8, 0.9]])

    # Вектор свободных членов
    b = np.array([0.1, 0.3, 0.5])

    # Проверка ранга матрицы и матрицы, расширенной вектором b
    rank_A = np.linalg.matrix_rank(A)
    rank_Ab = np.linalg.matrix_rank(np.column_stack((A, b)))

    if rank_A == rank_Ab:
        if rank_A == A.shape[1]:
            print('Система имеет единственное решение')
        else:
            print('Система имеет бесконечное множество решений.')
    else:
        print('Система не имеет решений')


def main():
    print("\n")
    print("\n")
    print("1) Найти решение системы: \n")
    task1()
    print("2)")
    task2()


main()
