def sayhello(*name):
    print("Hello {0} and {1}".format(*name))

def sayhello2(n1, n2):
    print("Hello {0} and {1}".format(n1, n2))


def main(names):
    sayhello(*names)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
