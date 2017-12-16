#!/usr/local/anaconda3/bin/python

def print_tables(x,y):
    for i in range(0,y):
        val = i * x
        print("{0} x {1} = {2}".format(x, i, val))

if __name__ == '__main__':
    print("Tables program to help you\n")
    x = input("Enter table number: ");
    y = input("Count of {0} tables: ".format(x))
    print_tables(int(x), int(y));
