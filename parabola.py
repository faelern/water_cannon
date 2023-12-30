import numpy as np
from math import pi
from vardata import *

# x1 - distance to target, y1 - target elevation


def calculate_polynomial(x1, y1):
    a = -(x1 ** 2 * G) / (2 * V ** 2)
    b = x1
    c = -(x1 ** 2 * G) / (2 * V ** 2) - y1 + CANNON_ELEVATION
    return a, b, c


def calculate_roots(a, b, c):
    roots = np.roots([a, b, c])
    return roots


def calculate_v_angle(x1, y1):
    a, b, c = calculate_polynomial(x1, y1)
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    else:
        root = min(calculate_roots(a, b, c))  # smaller root = smaller angle, preferred
        angle = np.arctan(root)
        if UNIT == 'deg':
            return angle * 180 / pi
        else:
            return angle

