#!/usr/local/anaconda3/bin/python

def shell_sort(data):
    N = len(data)
    M = int(N/2)
    while(1):
        for I in range(0, (N - M)):
            for J in range(I,-1,-M):
                if (data[J] > data[J+M]):
                    tmp = data[J]
                    data[J] = data[J+M]
                    data[J+M] = tmp
        M = int(M/2)
        if (M == 0):
            break
    return data
