#!/usr/local/anaconda3/bin/python

def run_xchng_sort(data):
    data_len = len(data)
    print("Length of data: {0}".format(data_len))
    for idx in range(0, data_len):
        for y in range(0, (data_len - 1)):
            if (data[y] > data[y+1]):
                tmp = data[y+1]
                data[y+1] = data[y]
                data[y] = tmp
    return data

