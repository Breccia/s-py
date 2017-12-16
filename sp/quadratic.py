#!/usr/local/anaconda3/bin/python

import matplotlib.pylab as plt

# 0 = -(x**2) -2x - 1

def plot_quad():
    x = []
    y = []
    for i in range(-50, 50):
        x.append(i)
        y.append(+(i ** 2) + (2*(i**1)) + 1)

    plt.plot(x, y, marker='*')
    plt.show()



if __name__ == '__main__':
    plot_quad()

