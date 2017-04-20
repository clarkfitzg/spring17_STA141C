def sayhello(n1, n2):
    print("Hello {0} and {1}".format(n1, n2))

def sayhello2(n1, n2):
    print("Hello {0} and {1}".format(n1, n2))


def main(n1, n2):
    sayhello(n1, n2)

print("Above the main")

if __name__ == "__main__":
    import sys
    n1, n2 = sys.argv[1:]
    # OR
    #n1 = sys.argv[1]
    #n2 = sys.argv[2]
    main(n1, n2)
