from math import cos, fabs, pi

def f(x):
    return -cos(x) * x * x

def method(a, b, delta, E):

    while (fabs(b - a) > E):
        x1 = (b + a) / 2 - delta * (b - a)
        x2 = (b + a) / 2 + delta * (b - a)
        if(f(x1) < f(x2)):
            b = x2
        else:
            a = x1
    return (a + b) / 2

print(method(0, pi/2, 0.25, 0.001))