def adder(x, y):
    return x + y


def main(x, y):
    print(adder(x, y))
    

if __name__ == "__main__":
    import sys
    x, y = [float(x) for x in sys.argv[1:]]
    main(x, y)
