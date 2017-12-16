#!/usr/local/anaconda3/bin/python

import math

def compute_median(num_list):
    list_len = len(num_list)
    num_list.sort()
    mid_idx = 0
    list_median = 0
    if (0 == (list_len % 2)):
        mid_idx = int(list_len/2)
    else:
        mid_idx = int((list_len + 1)/2)
    
    list_median = (num_list[mid_idx - 1] + num_list[mid_idx])/2
    print(num_list)
    print('Mid vals: {0},{1}'.format(num_list[mid_idx - 1], num_list[mid_idx]))
    print('Len : {0}, median: {1}'.format(list_len, list_median))

if __name__ == '__main__':
    print ('Trying to refresh my memory')
    num_list = [23,45,67,89,1,34,5,99,87]
    compute_median(num_list)
