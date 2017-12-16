#!/usr/local/anaconda3/bin/python

def ctof(c):
    f = ((float(c) * 9)/5) + 32
    return f

def ftoc(f):
    c = ((float(f) - 32) * 5)/9
    return c

if __name__ == "__main__":
    print("Unit converter [C <-> F (0/1) / inches <-> cm (2/3) / km <-> miles (4/5)]")
    ch = input("Enter your choice[0/1/2/3/4/5]: ")
    if (ch == "0"):
        c = input("Enter celcius: ")
        f = ctof(c)
        print("Celcius {0:.2f} = {1:.2f} F".format(float(c),float(f)))
    elif (ch == "1"):
        f = input("Enter farenheit: ")
        c = ftoc(f)
        print("Farenheit {0:.2f} = {1:.2f} C".format(float(f),float(c)))

