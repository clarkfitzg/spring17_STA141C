
from itertools import starmap

from multiprocessing import Pool

def f(x, y):
    return x * y

def f2(args):
    x, y = args
    return x * y


xy = list(map(f2, ((0, 1), (1, 2))))

xy = list(starmap(f, ((0, 1), (1, 2))))




if __name__ == "__main__":

    pool = Pool()
    fx = pool.starmap(f, zip(range(10), range(10)))

    fx = pool.map(f2, zip(range(10), range(10)))

    print(fx)
