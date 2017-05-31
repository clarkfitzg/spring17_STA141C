import numpy as np
from sklearn.datasets import load_svmlight_file


X, y  = load_svmlight_file("/Users/clark/data/news20.binary")

w0 = np.zeros(X.shape[1])

def f(w, lamb):
    """
    Eq. (2) in problem 2

    Non-vectorized, slow
    """
    total = 0
    nrows = X.shape[0]
    for i in range(nrows):
        current = 1 + np.exp(-y[i] * X[i, ].dot(w))
        total += np.log(current)
    total += (lamb / 2) * w.dot(w)
    return total

f(w0, 1)


def f2(w, lamb):
    """
    Eq. (2) in problem 2

    Vectorized (no explicit loops), fast
    """
    yxTw = y * X.dot(w)
    firstpart = np.log(1 + np.exp(-yxTw))
    total = firstpart.sum()
    total += (lamb / 2) * w.dot(w)
    return total

f2(w0, 1)
