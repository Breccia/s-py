#!/usr/local/anaconda3/bin/python

import matplotlib.pylab as plt
import math
import random

# Projectile Motion graph
# Horizontal velocity = Uh cos(x)
# Vertical velocity = Uv sin(x) - gt
# Velocity change on x, Vh = Uh cos(x) t
# Velocity change on y, Vv = Uv sin(x) t - (0.5) g(t**2)

# Time to reach max height is when Vertical velocity goes 0
# 0 = Uv sin(x) - gt
# Time to reach max height, t = (Uv sin(x))/g
# Total time travelled = 2t => 2(Uv sin(x))/g

# Input values
# Velocity U
# Angle of trajectory x
# constant gravity g = 9.8 m/s

g = 9.8

def frange(start, stop, interval):
    numbers = []
    while (start < stop):
        numbers.append(start)
        start = start + interval

    return numbers


def plot_projectile_motion(angle, velocity):
    angle_radians = math.radians(float(angle))
    velocity_float = float(velocity)
    time_travelled = (2 * velocity_float * math.sin(angle_radians))/g
    h_change = []
    v_change = []
    for t in frange(0, time_travelled, 0.1):
        h_change.append(velocity_float * math.cos(angle_radians) * t)
        v_change.append(((velocity_float * math.sin(angle_radians) * t) - ((0.5) * g * (t**2))))

    plt.plot(h_change, v_change, marker='*')
    plt.title('Projectile Motion')
    plt.xlabel('Horizontal velocity')
    plt.ylabel('Vertical velocity')
    plt.show()


if __name__ == '__main__':
    print('Projective motion graph\n')
    angle = input('Enter angle of throw: ')
    velocity = input('Enter velocity: ')

    plot_projectile_motion(angle, velocity)
