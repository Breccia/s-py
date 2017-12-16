#!/usr/local/anaconda3/bin/python

# BSC - 3.2 Exchange sort

values = [10, 3, 14, 17, 2, 11]

def xsort(val):
    size = len(val)
    orig = val
    for i in range(0,size):
        print("Printing values %d" % val[i])
        for j in range(i+1, size):
            if (val[i] > val[j]):
                T = val[i]
                val[i] = val[j]
                val[j] = T
    print("Printing input vals: {0}".format(val))
    print("Printing sorted vals: {0}".format(sorted))

if __name__ == '__main__':
    print('Phew!')
    xsort(values)

