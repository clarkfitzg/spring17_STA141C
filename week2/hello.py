#!/usr/bin/env python

def countlines(file):
    """
    Count the lines in file. file is a string representing the file to
    open.
    """
    with open(file) as f:
        nlines = 0
        for line in f:
            nlines += 1
        return nlines


def main(myname, file):
    print("Hello {0}".format(myname))
    nlines = countlines(file)
    print("There are {0} lines in {1}".format(nlines, file))


if __name__ == "__main__":
    import sys
    myname = sys.argv[1]
    file = sys.argv[2]
    main(myname, file)
