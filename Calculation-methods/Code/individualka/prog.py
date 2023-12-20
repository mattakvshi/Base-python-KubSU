from SecondaryFunc import *
from matplotlib.pyplot import *
from scipy.linalg import *
from seaborn import *
from pandas import *


print("Select scheme: explicit(1), implicit(2)\n\nChoice:", end="")
c = int(input())
# c = 2
if (c == 1):
    print("\n===== Explicit solution scheme =====\n")
    n = 100  # для t
    m = 35  # для x
    T = 1

    x = linspace(0, pi / 2, m)
    t = linspace(0, T, n)

    h = (pi / 2) / m
    tau = T / n

    net = netInit(m, n)
    netBorders(net, m, n, x, t)

    # если меньше 0.5, то сразу рушится
    print(tau / (h ** 2))

    for i in range(n - 1):
        for j in range(1, m - 1):
            net[i + 1][j] = (tau * ((net[i][j + 1] - 2 * net[i][j] + net[i][j - 1]) / (h * h))) + net[i][j]

    netAnalytical = netInit(m, n)
    netAnalitycFunc(netAnalytical, m, n, x, t)

    netError = netInit(m, n)
    netErrorFunc(netError, net, netAnalytical, m, n)

    net_df = DataFrame(net)
    net_analytical_df = DataFrame(netAnalytical)
    net_error_df = DataFrame(netError)

    figure(figsize=(18, 6))

    subplot(1, 3, 1)
    heatmap(net_df, cmap='viridis', xticklabels=round(m / 10), yticklabels=round(n / 10))
    title('Heatmap of the net matrix')
    xlabel('Space (x)')
    ylabel('Time (t)')

    subplot(1, 3, 2)
    heatmap(net_analytical_df, cmap='viridis', xticklabels=round(m / 10), yticklabels=round(n / 10))
    title('Heatmap of the netAnalytics matrix')
    xlabel('Space (x)')
    ylabel('Time (t)')

    subplot(1, 3, 3)
    heatmap(net_error_df, cmap='coolwarm', xticklabels=round(m / 10), yticklabels=round(n / 10))
    title('Heatmap of the netError matrix')
    xlabel('Space (x)')
    ylabel('Time (t)')
    tight_layout()
    show()
else:
    print("\n===== Implicit solution scheme =====\n")
    n = 500 # для t
    m = 500  # для x
    T = 1

    x = linspace(0, pi / 2, m)
    t = linspace(0, T, n)

    h = (pi / 2) / m
    tau = T / n
    lmbd = tau / (h ** 2)

    net = netInit(m, n)
    netBorders(net, m, n, x, t)

    print(tau / (h ** 2))

    slau = netInit(m, m)
    f = [0] * m

    for i in range(n - 1):
        for j in range(1, m - 1):
            slau[j][j] = -(1 + 2 * lmbd)
            f[j] = -1 * net[i][j]

        f[0] = net[i + 1][0]
        slau[0][0] = 1
        slau[0][1] = 0

        slau[m - 1][m - 2] = 0
        #из-за этого условия пробой
        slau[m - 1][m - 1] = 1
        f[m - 1] = net[i][m - 1]

        for j in range(1, m - 1):
            slau[j][j + 1] = lmbd
            slau[j][j - 1] = lmbd

        # for j in range(m):
        #     print(slau[j])
        # print()
        # print(f)
        # print(net[i])
        # print()

        temp = solve(slau, f)
        for j in range(1, m - 1):
            net[i + 1][j] = temp[j]

    # printNet(net, n)

    netAnalytical = netInit(m, n)
    netAnalitycFunc(netAnalytical, m, n, x, t)

    netError = netInit(m, n)
    netErrorFunc(netError, net, netAnalytical, m, n)

    net_df = DataFrame(net)
    net_analytical_df = DataFrame(netAnalytical)
    net_error_df = DataFrame(netError)

    figure(figsize=(18, 6))

    subplot(1, 3, 1)
    heatmap(net_df, cmap='viridis', xticklabels=round(m / 10), yticklabels=round(n / 10))
    title('Heatmap of the net matrix')
    xlabel('Space (x)')
    ylabel('Time (t)')

    subplot(1, 3, 2)
    heatmap(net_analytical_df, cmap='viridis', xticklabels=round(m / 10), yticklabels=round(n / 10))
    title('Heatmap of the netAnalytics matrix')
    xlabel('Space (x)')
    ylabel('Time (t)')

    subplot(1, 3, 3)
    heatmap(net_error_df, cmap='coolwarm', xticklabels=round(m / 10), yticklabels=round(n / 10))
    title('Heatmap of the netError matrix')
    xlabel('Space (x)')
    ylabel('Time (t)')
    tight_layout()
    show()