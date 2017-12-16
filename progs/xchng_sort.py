#!/usr/local/anaconda3/bin/python

import sys
sys.path.insert(0, "../libs")
from spy_xchng_sort import run_xchng_sort

if __name__ == '__main__':
    #data_set = [45, 6, 2, 89, 32,6, 87, 23, 98, 42]
    data_set = []
    print("Exchange Sort")
    count = input("Enter total number of data: ")
    idx = 0
    for idx in range(0, int(count)):
        val = input("Enter val {0}:".format(idx + 1))
        data_set.append(int(val))
    print("Input: {0}".format(data_set))
    sort_set = run_xchng_sort(data_set)
    print("Sorted: {0}".format(sort_set))
