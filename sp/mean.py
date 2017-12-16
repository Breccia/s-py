#!/usr/local/anaconda3/bin/python

import math

def compute_mean(num_list):
    list_len = len(num_list)
    list_sum = sum(num_list)
    list_mean = list_sum/list_len
    print('Computed mean for list len = {0}, sum = {1}, mean = {2}'.format(list_len, list_sum, list_mean))

if __name__ == '__main__':
    print ('Trying to refresh my memory')
    num_list = [23,45,67,89,1,34,5]
    compute_mean(num_list)
