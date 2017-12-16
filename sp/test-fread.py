#!/usr/local/anaconda3/bin/python

import csv
import matplotlib.pyplot as plt

def plot_csv(col1, col2):
    plt.plot(col1, col2)
    plt.show()

def csv_read_test(fName):
    lineNo = 0
    col1 = []
    col2 = []
    with open(fName) as f:
        cr = csv.reader(f)
        for row in cr:
            print("{0} -> {1}".format(row[0], row[1]))
            col1.append(int(row[0]))
            col2.append(int(row[1]))
    col1_sum = sum(col1)
    col2_sum = sum(col2)
    col1_avg = col1_sum/len(col1)
    col2_avg = col2_sum/len(col2)
    print ("Col1: [%d] [%d] [%d]" % (col1_sum, col1_avg, len(col1)))
    print ("Col2: [%d] [%d] [%d]" % (col2_sum, col2_avg, len(col2)))
    plot_csv(col1, col2)
    #print('Col1 [sum] [avg] [len] = [{0}] [{1}], Col2 [sum] [avg] [len] = [{2}] [{3}]'.format(col1_sum, len(col1), col2_sum

def read_test(fName):
    lineNo = 0
    with open(fName) as f:
        for line in f:
            lineNo = lineNo + 1
            print("{0}: {1}".format(lineNo, line))


if __name__ == '__main__':
    print("Remember this... the main() version of python")
    read_test("./test.csv")
    csv_read_test("./test.csv")
