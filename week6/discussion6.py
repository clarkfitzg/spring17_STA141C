# Notes from interpreter
# coding: utf-8
sentence = "The quick brown fox jumps over the lazy dog."
sentence
sentence.split()
from collections import Counter
pairs = Counter()
pairs
"The", "the"
pairs[["a", "b"]] = 1
t = ("The", "quick")
t
type(t)
hash(t)
pairs[t] = 1
pairs
pairs[t] += 1
pairs
sentence.split()
words = Counter(sentence.split())
words
get_ipython().magic('clear ')
import numpy as np
A = np.array([3, 0, 0, 0]).reshape((2, 2))
A
x = np.array([1, 0])
x
A.dot(x)
np.linalg.eig(A)
get_ipython().magic('pinfo np.linalg.eig')
get_ipython().set_next_input('evals, evecs = np.linalg.eig');get_ipython().magic('pinfo np.linalg.eig')
evals, evecs = np.linalg.eig(A)
evals
evecs
A = np.array([3, 0, 0, 0]).reshape((2, 2))
A = np.zeros(3, 3)
A = np.zeros((3, 3))
A
A[0, 0] = 75
A
evals, evecs = np.linalg.eig(A)
evals
evecs
A.dot((0, 1, 1))
A
from scipy.sparse import csr_matrix
A2 = csr_matrix(A)
A
A2
A2.dot((0, 1, 1))
A2 + 5
A + 5
A2
e = np.ones(3)
e
e.T()
e.T
e.shape = (3, 1)
e
e.dot(e.T)
eeT = e.dot(e.T)
eeT
eeT.dot(x)
x
A
x = np.ones(3)
x
x = np.random.randn(3)
x
(A + eeT).dot(x)
eeT
eeT
A.dot(x)
A2.dot(x)
eeT.dot(x)
x.sum()
x.sum() * np.ones(length(x))
x.sum() * np.ones(len(x))
smd = {}
smd[(0, 1)] = 745
smd
A2
3 * A2
A3 = 3 * A2
A3.todense()
from scipy.sparse import linalg
linalg.eigs(A2)
linalg.eigs(A2, k = 1)
a, b = linalg.eigs(A2, k = 1)
a
b
eval
evals
evecs
get_ipython().magic('save discussion6')
