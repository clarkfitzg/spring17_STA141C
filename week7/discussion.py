import numpy as np

from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split

from sklearn.linear_model import Ridge

from sklearn.preprocessing import normalize, scale


X, y  = load_svmlight_file("/Users/clark/data/news20.binary")



w = np.random.randn(X.shape[1])

# w^T x_i
x0w = X[0, ].dot(w.T)


Xtrain, Xtest = train_test_split(X, test_size = 0.2)


def mse(ypredict, ytrue):
    """
    >>> mse(1.0, 3.0)
    4.0
    """
    diff = ypredict - ytrue
    return np.mean(diff**2)


n = 20

income = 10**6 + np.random.randn(n) * 100000
children = np.random.choice([0, 1, 2, 3, 4], size=n)

X = np.stack([income, children]).T
w = np.array([10, 11])

noise = 1000 * np.random.randn(n)

y = X.dot(w) + noise

model = Ridge(alpha = 1.0)
model.fit(X, y)

X2 = scale(X, axis = 0)

y2 = y.reshape((n, 1))
y2 = scale(y2, axis = 0)

model2 = Ridge(alpha = 1.0)
model2.fit(X2, y2)


