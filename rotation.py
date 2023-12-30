from vardata import *
from math import pi

def calculate_h_angle(pos):
    h_angle = pos * HFOV / XRES
    if UNIT == 'deg':
        return h_angle
    else:
        return h_angle * pi / 180



