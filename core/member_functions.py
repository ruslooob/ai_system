import numpy as np


def z_member_func(x, a, b):
    if x < a:
        return 1
    elif a <= x <= b:
        return -1 * (x - a) / (b - a) + 1
    else:
        return 0


def s_member_func(x, a, b):
    if x < a:
        return 0
    elif a <= x < b:
        return (x - a) / (b - a)
    else:
        return 1


def triangle_member_func(x, a, e, c):
    if x < a:
        return 0
    elif a <= x < e:
        return (x - a) / (e - a)
    elif e <= x < c:
        return (c - x) / (c - e)
    return 0


def trapezoid_member_func(x, a, b, c, d):
    if a <= x < b:
        return (x - a) / (b - a)
    elif b <= x < c:
        return 1
    elif c <= x < d:
        return (d - x) / (d - c)
    return 0


def gauss_member_func(x, mean, std):
    return np.exp(-(x - mean) ** 2 / (2 * std ** 2))
