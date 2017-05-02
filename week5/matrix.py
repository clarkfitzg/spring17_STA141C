import numpy as np
import scipy


# Frobenius norm
############################################################
n = 6
A = np.eye(n)

expected = np.sqrt(n)
actual = np.linalg.norm(A, ord="fro")

# Question: Is this comparison a good idea?
expected == actual


# CSR sparse matrix
############################################################

from scipy.sparse import csr_matrix

# 1 is a "hub", linking to many others
# 3 is an "authority", with many incoming links
# TODO: draw this
from_id =   (1, 1, 1, 1, 1, 2, 4)
to_id =     (0, 2, 3, 4, 5, 3, 3)
vals = np.ones(len(from_id))

# Question: What's the most efficient data type to represent this adjacency matrix?

A2 = csr_matrix((vals, (from_id, to_id)), shape=(n, n))

# Check it looks reasonable
A2.todense()

# Matrix vector multiplication
x = np.arange(n)
A2.dot(x)
# with newest versions:
# A2 @ x

# Question: How large are A and A2?
# Then what is the time complexity for matrix vector multiplications in the
# sparse versus non sparse cases?


# Singular values
############################################################
# Use the sparse versions of the algorithms
# https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html

import scipy.sparse.linalg

# So what are these objects?
A2svd = scipy.sparse.linalg.svds(A2, k = 2)

# Verify: 'As we learned in the class, the leading right singular vector
# corresponds to the “authority” score of a web page.'


