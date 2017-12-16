#!/usr/local/anaconda3/bin/python

import matplotlib.pylab as plt

def fibo(n):
    series = []
    ratio = []
    x = []
    start = 0
    if (n == 0):
        series = [0]
        x = [0]
        ratio = [0]
        return x,series,ratio
    elif (n == 1):
        series = [0]
        x = [0]
        ratio = [0]
        return x,series,ratio
    elif (n == 2):
        series = [0,1]
        x = [0,1]
        ratio = [0,0]
        return x,series,ratio
    a = 0 
    b = 0
    c = 0
    print('Start = {0}, n = {1}'.format(start, n))
    for i in range(start, n):
        x.append(i)
        if (i == 0):
            c = 0
            r = 0
            a = 0
            b = 0
        elif (i == 1):
            c = 1
            r = 0
            a = 1
            b = 0
            print('a={0}, b = {1}, c = {2}, i = {3}'.format(a,b,c,i))
        else:
            c = a + b
            r = (c/a)
            b = a
            a = c

        series.append(c)
        ratio.append(r)
        print('c = {0}, r = {1}'.format(c,r))

    return x,series,ratio

def plot_fibo(x, y, z):
    #plt.plot(x,y)
    plt.plot(x,z)
    plt.show()

if __name__ == '__main__':
    n = input('Enter fibo series number n: ')
    x,y,z = fibo(int(n))
    print(x,y)
    plot_fibo(x, y, z)
        
