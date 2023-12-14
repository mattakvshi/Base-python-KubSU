import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import CubicSpline
from scipy.integrate import quad

f = lambda t: np.exp(-t ** 2)

x = np.linspace(0, 2, 100)
plt.plot(x, f(x))


def my_erf(x, n=1000):
    h = x / n
    res = 0

    for i in range(n):
        res += f(i * h)

    res *= 2 / math.sqrt(math.pi) * h

    return res


for i in range(21):
    print(f"{i * 0.1:.1f}: {my_erf(i * 0.1):.5f} {math.erf(i * 0.1):.5f}")

f = lambda x: 4 / (1 + x * x)

x = np.linspace(0, 1, 100)
plt.plot(x, f(x))


def trap_pi(n=1000):
    h = 1 / n
    res = 0.5 * (f(0) + f(1))

    for i in range(1, n):
        res += f(i * h)

    return res * h


def rect_pi(n=1000):
    h = 1 / n
    res = 0

    for i in range(n):
        res += f((i + 0.5) * h)

    return res * h


for i in [8, 32, 128]:
    t1 = trap_pi(i)
    t2 = rect_pi(i)
    print(f"n = {i} - Rect: {t1:.6f} AE: {abs(math.pi - t1):.6f}; Trap: {t2:.6f} AE: {abs(math.pi - t2):.6f}")



for i in [8, 32, 128]:
    x = np.linspace(0, 1, i)
    cs = CubicSpline(x, f(x))
    t = cs.integrate(0, 1)
    print(f"n = {i} - Spline: {t:.15f} AE: {abs(math.pi - t):.15f}")



f = lambda x: np.where(x <= 2, np.exp(x*x), 1/(4 - np.sin(16*np.pi*x)))
ans = 16.969025545
res, er = quad(f, 0, 4, limit=100)
print(f"Ans: {res}; AE: {abs(ans-res)};")


N = 10000000
x = np.linspace(0, 4, N)
cs = CubicSpline(x, f(x))
# Вычисление интегралов на двух интервалах
res = cs.integrate(0, 4)

print(f"Ans: {res}; AE: {abs(ans-res)}")