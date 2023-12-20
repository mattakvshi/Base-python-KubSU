from numpy import *


def netInit(mx, nt):
    net = [0.0] * nt
    for i in range(nt):
        net[i] = [0.0] * mx

    return net


def netBorders(net, mx, nt, x, t):
    for i in range(mx):
        net[0][i] = sin(x[i])

    for i in range(1, nt):
        net[i][0] = 0.0

    for i in range(1, nt):
        net[i][mx - 1] = exp(-1 * t[i])


def netAnalitycFunc(net, mx, nt, x, t):
    for i in range(nt):
        for j in range(mx):
            net[i][j] = exp(-1 * t[i]) * sin(x[j])

def netErrorFunc(netError, net, netAnalytical, mx, nt):
    for i in range(nt):
        for j in range(mx):
            netError[i][j] = net[i][j] - netAnalytical[i][j]


def printNet(net, nt):
    for i in range(nt - 1, -1, -1):
        print(net[i])
