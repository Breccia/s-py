#!/usr/local/anaconda3/bin/python

import sys

sys.path.insert(0, "../libs/")
from spy_mean import compute_mean

if __name__ == "__main__":
    print("Program to compute mean")
    count = input("Enter total number of samples: ")
    idx = 0
    data = []
    for idx in range(0, int(count)):
        val = input("Enter data {0}: ".format(idx + 1))
        data.append(val)
    #mean = spy_mean.compute_mean(data)
    mean = compute_mean(data)
    print("You entered: {0} vals, mean = {1}".format(count, mean))


