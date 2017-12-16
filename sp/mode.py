#!/usr/local/anaconda3/bin/python

import math
from collections import Counter

def compute_mode(x):
    c = Counter(x)
    return c.most_common()[0]

def print_frequency_table(x):
    c = Counter(x)
    tot = len(c)
    print('Value\tFrequency')
    for i in range(0, tot):
        value = c.most_common()[i][0]
        freq = c.most_common()[i][1]
        print('{0}\t{1}'.format(value, freq))


if __name__ == '__main__':
    print('Hurrah! I still remember this piece')
    x = [34,5,32,1,3,3,54,7,3,5,6,5,4,3,4,4,3,3,5,6,7,7,5,4,3,5,6,3,8,99,7,65,5,4,4,56,7]
    val,count = compute_mode(x)
    print(x)
    print('Total elements: {0}, val: {1}, frequency: {2}'.format(len(x), val, count))
    print_frequency_table(x)

