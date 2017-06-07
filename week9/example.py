
import multiprocessing as mp

def f(x):
    return x**2

pool = mp.Pool(processes=4)

results = pool.map(f, range(4))

print(results)
