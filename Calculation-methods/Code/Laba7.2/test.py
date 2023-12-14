import numpy as np
import matplotlib.pyplot as plt
import math

func = lambda x : (2/np.sqrt(np.pi))*np.exp(-x ** 2)

x = np.linspace(0, 2, 100)
plt.plot(x, func(x))

N = 1000

def euler_method(x_end):
    y_values = [0]  # начальное условие y(0) = 0
    h = x_end/N
    x = 0
    for i in range(1, N+1):
        y_new = y_values[i-1] + h * func(x)
        x += h
        y_values.append(y_new)

    return y_values

x_vals = list(range(21))
y_vals = euler_method(2)
# for i in range(len(y_vals)):
#     print(i, y_vals[i])
# plt.plot(x_vals, y_vals)

for i,j in zip(x_vals, y_vals[::N//20]):
    print(f"{i*0.1:.1f}: {j:.5f} {math.erf(i*0.1):.5f}")

# Погрешность O(h^2)


a = 1

# r = [100]
# f = [100]

r = [20]
f = [20]


# r = [15]
# f = [22]

# r = [1]
# f = [1]

rab = lambda t: 2*r[t] - a*r[t]*f[t]
fox = lambda t: -f[t] + a*r[t]*f[t]

t_end = 20
N = 1000


def sim():
    h = t_end/N
    for i in range(1, N):
        r.append(r[-1] + h * rab(i-1))
        f.append(f[-1] + h * fox(i-1))

sim()

t = np.linspace(0, t_end, N)

plt.plot(t, r, 'tab:blue')
plt.plot(t, f, 'tab:orange')



print(f[-1])
print(r[-1])