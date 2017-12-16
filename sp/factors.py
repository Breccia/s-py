#!/usr/local/anaconda3/bin/python

def is_factor(x,y):
    if (x % y):
        return 0
    return 1

if __name__ == '__main__':
    print("Running code to check factor of input given\n")
    x = input("Enter value for x: ")
    y = input("Enter value for y: ")
    z = is_factor(int(x),int(y))
    print("Factor({0},{1}) = {2}\n".format(x,y,z))
