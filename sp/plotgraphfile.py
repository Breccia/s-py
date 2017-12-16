#!/usr/local/anaconda3/bin/python

import csv
import math
import matplotlib.pyplot as plt

def plot_graph(x,y):
    plt.scatter(x,y)
    plt.xlabel('Time')
    plt.ylabel('Distance')
    plt.show()

# R = (n * sum(x.y) - sum(x).sum(y))/sqrt(((n * sum(x**2) - (sum(x))**2))((n * sum(y**2) - (sum(y))**2)))

def compute_correlation(x,y):
    data_len = min(len(x), len(y))
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x_sq = 0
    sum_y_sq = 0
    for m,n in zip(x,y):
        sum_xy = (sum_xy + (m * n))
        sum_x = (sum_x + m)
        sum_y = (sum_y + n)
        sum_x_sq = (sum_x_sq + (m ** 2))
        sum_y_sq = (sum_y_sq + (n ** 2))
    R = ((data_len * sum_xy) - (sum_x * sum_y))/math.sqrt(((data_len * sum_x_sq) - (sum_x ** 2)) * ((data_len * sum_y_sq) - (sum_y ** 2)))
    print('R = {0}'.format(R))

def read_and_plot():
    with open("test.csv") as f:
        reader = csv.reader(f)
        next(reader)
        x = []
        y = []
        for row in reader:
            x.append(int(row[0]))
            y.append(int(row[1]))

        compute_correlation(x,y)
        plot_graph(x,y)

if __name__ == '__main__':
    read_and_plot()
