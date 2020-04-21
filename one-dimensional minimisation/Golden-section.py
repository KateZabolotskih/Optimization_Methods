from math import cos, fabs, pi, sqrt

def f(x):
    return -cos(x) * x * x

def method(a, b, E):
    K = (1 + sqrt(5))/ 2
    lam = b - (b - a) / K
    mu = a + (b - a) / K
    y1 = f(lam)
    y2 = f(mu)

    while (fabs(b - a) > E):
        if (y1 > y2):
            a = lam
            lam = mu
            y1 = y2
            mu = a + (b - a) / K
            y2 = f(mu)
        else:
            b = mu
            mu = lam
            y2 = y1
            lam = lam = b - (b - a) / K
            y1 = f(lam)

    return (b + a) / 2

print(method(0, pi / 2, 0.001))



