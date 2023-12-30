from parabola import calculate_v_angle
from rotation import calculate_h_angle
from math import sin, cos
from vardata import *


# pos - x coordinate of object on camera
# distance - relative distance from camera to object
# abs_distance - absolute distance from camera plane to object
# elevation - height of object


def calculate_abs_distance(y_pos, distance):
    angle = y_pos * VFOV / YRES
    return cos(angle) * distance


def calculate_elevation(y_pos, distance):
    angle = y_pos * VFOV / YRES
    return INIT_ELEVATION - sin(angle) * distance


def aim(x_pos, y_pos, distance):
    elevation = calculate_elevation(y_pos, distance)
    abs_distance = calculate_abs_distance(y_pos, distance)
    h_angle = calculate_h_angle(x_pos)
    v_angle = calculate_v_angle(abs_distance, elevation)

    return h_angle, v_angle


print(aim(300, 0, 3))
