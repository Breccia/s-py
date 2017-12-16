#!/usr/local/anaconda3/bin/python

# program to plot Gravitational Force vs Distance graph
# Newton's Universal Gravitational Law

import matplotlib.pyplot as plt

# F = Gm1m2/r^2

# Gravitational constant
G = 6.674 * (10**-11) #m^3/kg.s^2

def plot_graph(m1, m2, d_min, d_max):
    print("User input mass 1 = {0} kg, mass 2 = {1} kg\n".format(m1, m2))
    d_intvl = 1
    if ((d_max - d_min)/10 >= 10):
        d_intvl = 10
    distance = range(d_min, d_max, d_intvl)
    Force = []
    for i in distance:
        Force.append((G*m1*m2)/(i * i))
    plt.plot(distance, Force, marker='*')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()

def get_user_input():
    m1 = input("Enter mass 1 in kg: ");
    m2 = input("Enter mass 2 in kg: ");
    d_min = input("Enter distance min: ");
    d_max = input("Enter distance max: ");

    return m1,m2,d_min,d_max


if __name__ == '__main__':
    print('G = {0}'.format(G))
    m1,m2,d_min,d_max = get_user_input()
    plot_graph(float(m1), float(m2), int(d_min), int(d_max))

