
from math import sqrt

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


print("Введите коэффициенты уравнения\n")
a = float(input("а = "))
b = float(input("b = "))
c = float(input("c = "))
print("\n")


print("Заданное уравнение: ({})x^2 + ({})x + ({}) = 0".format(a, b, c) + "\n")

d = b**2 - (4*a*c)

if d < 0:
    print("Дискриминант меньше 0, корней нет." + "\n")
elif d == 0:
    x = -b / (2*a)
    print("Дискриминант равен 0, корень: x = {}".format(x) + "\n")
else:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)
    print("Дискриминант больше 0, корни: x1 = {}, x2 = {}".format(x1, x2) + "\n")

# Вычисление через сигнум
if b != 0:
    if d != 0:
        x1 = -2*c / (sign(b) * (abs(b) + sqrt(d)))
        x2 = -2*c / (sign(b) * (abs(b) - sqrt(d)))
    else:  # d == 0
        x1 = -c / b
        x2 = None
else:  # b == 0
    if d != 0:
        x1 = sqrt(abs(2*c/a))
        x2 = -sqrt(abs(2*c/a))
    else:  # d == 0
        x1 = sqrt(abs(c/a))
        x2 = -sqrt(abs(c/a))

print("Вычисление через сигнум:")
if x2 is not None:
    print("Корни: x1 = {}, x2 = {}".format(x1, x2) + "\n")
else:  # x2 is None
    print("Корень: x = {}".format(x1) + "\n")