#!/usr/local/anaconda3/bin/python

def compute_mean(input_data):
    tot_entries = len(input_data)
    idx = 0
    sum = 0
    mean = 0
    for idx in range(0, tot_entries):
        sum = sum + float(input_data[idx])
    mean = sum/tot_entries
    return mean


