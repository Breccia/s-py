#!/usr/local/anaconda3/bin/python

def frange(start, stop, interval):
    numbers = []
    cntr = start
    while (cntr < stop):
        numbers.append(cntr)
        cntr = cntr + interval

    return numbers

if __name__ == "__main__":
    numbers = frange(0.0, 3.0, 0.2)
    for i in numbers:
        print ('{0:.2f}'.format(i))


