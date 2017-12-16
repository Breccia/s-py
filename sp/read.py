#!/usr/local/anaconda3/bin/python

def parse_csv(fileName):
    print("Parsing CSV {0}".format(fileName))
    lineNo = 0
    with open(fileName) as f:
        for line in f:
            print(line)
            lineNo = lineNo + 1
            if (1 == lineNo):
                return 0
        
    

if __name__ == '__main__':
    print("This is how python main starts");
    parse_csv("./FL_insurance_sample.csv");

