
import math
import time

from task4 import task4


#Для Х по модулю меньше 1


def calculateFirstRow(k, x):
    return (1 / (math.sqrt(math.pow(k, 3) + x)))

def calculaterSecondRow(k, x):
    return (1 / (math.sqrt(math.pow(k, 3) - x)))


def main():
    arrayX = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    firstRow = 0
    secondRow = 0
    K = int(input("Введите кол-во операций: "))
    print("\n")

    print("A) Каждый ряд сходится: \n")
    beginPoint = time.perf_counter()
    for i in range(0, len(arrayX), 1):
        for j in range(1,K, 1):
            firstRow += calculateFirstRow(K, arrayX[i])
            secondRow += calculaterSecondRow(K, arrayX[i])
        mainRow = firstRow - secondRow
        print("Х = " + str(arrayX[i]) + " и кол-ва операций " + str(K) + " результат: " + str(mainRow))
        firstRow, secondRow, mainRow = 0, 0, 0
    endPoint = time.perf_counter()
    print("\n")
    print("Б) Примерно " + str(K) + " членов ряда понадобиться, чтобы просуммировать его с ошибкой по модулю меньшей e.")
    print("\n")
    print("В) Оценка времени для обоих рядов при " + str(K) + f" операциях:  {endPoint - beginPoint:0.4f}")
    print("\n")

    for i in range(1, K, 1):
        firstRow += calculateFirstRow(K, 0.999999999)
        secondRow += calculaterSecondRow(K, 0.999999999)
    print("Д) s(x) для x = 0.5 и x = 0.999999999: " + str(firstRow - secondRow))


if __name__ == "__main__":
    main()
    task4()