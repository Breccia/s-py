#!/usr/local/anaconda3/bin/python

import sys

sys.path.insert(0, "../libs")

from spy_shell_sort import shell_sort

if __name__ == '__main__':
    test_data = [23, 5, 1, 65, 3, 1, 20, 34,56,78,90,12]
    print("Shell sort aka merge-xchng sort")
    print("Length of given  data: {0}, data={1}".format(len(test_data), test_data))
    sorted = shell_sort(test_data)
    print("Length of sorted data: {0}, data={1}".format(len(sorted), sorted))

