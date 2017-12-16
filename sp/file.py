#!/usr/local/anaconda3/bin/python

def read_data_from_file():
    with open("test.txt") as f:
        lineno = 0
        for line in f:
            lineno = (lineno + 1)
            print('Line: {0}, String: {1}'.format(lineno, line))

if __name__ == '__main__':
    print('Nice! I still remember this piece!');
    read_data_from_file()
