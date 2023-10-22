
import math

def originalRowCalculate(n):
    rowSum = 0
    for i in range(1, n + 1):
        rowSum += 1 / (math.pow(i, 2) + 1)

    return (rowSum)

def transformedRowCalculate(n):
    rowSum = 0
    for i in range(1, n + 1):
        rowSum += 1 / (math.pow(i, 4) * (math.pow(i, 2) + 1))
    rowSum = (math.pow(math.pi, 2) / 6) - (math.pow(math.pi, 4) / 90) + rowSum

    return (rowSum)

def task4():
    n = int(input("Введите кол-во операций: "))

    print("ОБЫЧНЫЙ ряд от " + str(n) + " операций: " + str(originalRowCalculate(n)))

    print("ПРЕОБРАЗОВАННЫЙ ряд от " + str(n) + " операций: " + str(transformedRowCalculate(n)))

    print("Разница в вычислениях составляет " + str(transformedRowCalculate(n) - originalRowCalculate(n)))

    # Хороший результат получаем для 1000000 операций


