import multiprocessing as mp
from sklearn.datasets import load_svmlight_file
import numpy as np
import time

from numba import jit
from scipy.spatial import cKDTree

traindata = load_svmlight_file("a9a.subset.train")
testdata = load_svmlight_file("a9a.subset.test")
Xtrain = traindata[0].todense()
ytrain = traindata[1]
Xtest = testdata[0].todense()
ytest = testdata[1]

"""
data to map over:
data = [
(Xtrain, ytrain, Xtest_1, ytest_1)
(Xtrain, ytrain, Xtest_2, ytest_2)
(Xtrain, ytrain, Xtest_3, ytest_3)
(Xtrain, ytrain, Xtest_4, ytest_4)
]
"""

@jit(nopython=True)
def go_nn_jit(Xtrain, ytrain, Xtest, ytest):
    """
    Compiled version- runs in 4.4 sec
    """
    correct =0
    for i in range(Xtest.shape[0]): ## For all testing instances
        nowXtest = Xtest[i,:]
        ### Find the index of nearest neighbor in training data

        # Initialize with the first row
        dis_smallest = np.linalg.norm(Xtrain[0,:]-nowXtest) 
        idx = 0

        for j in range(1, Xtrain.shape[0]):
            dis = np.linalg.norm(nowXtest-Xtrain[j,:])
            if dis < dis_smallest:
                dis_smallest = dis
                idx = j
        ### Now idx is the index for the nearest neighbor
        
        ## check whether the predicted label matches the true label
        if ytest[i] == ytrain[idx]:  
            correct += 1
    acc = correct/float(Xtest.shape[0])
    return acc


def go_nn_vec(Xtrain, ytrain, Xtest, ytest):
    """
    Vectorized version
    """
    pass


# A little unfair to the timings to build the tree separately, but oh well
tree = cKDTree(Xtrain, balanced_tree=True)


def go_nn_kdtree(eps=0, parallel=True):
    """
    Using a specialized data structure, the KDTree

    This is not as performant because we're in a high dimensional space

    0.777 accuracy? Should be 0.794
    """
    n_jobs = 1
    if parallel:
        n_jobs = -1

    neighbors = tree.query(Xtest, eps=eps, n_jobs=n_jobs)
    predictions = ytrain[neighbors[1]]

    acc = np.equal(predictions, ytest).mean()
    return acc




start_time = time.time()
acc = go_nn_jit(Xtrain, ytrain, Xtest, ytest)
print("Compiled version:")
print("Accuracy %lf Time %lf secs.\n"%(acc, time.time()-start_time)) 


start_time = time.time()
acc = go_nn_kdtree(parallel=False)
print("KDtree:")
print("Accuracy %lf Time %lf secs.\n"%(acc, time.time()-start_time)) 


start_time = time.time()
acc = go_nn_kdtree(parallel=True)
print("Parallel KDtree:")
print("Accuracy %lf Time %lf secs.\n"%(acc, time.time()-start_time)) 


start_time = time.time()
acc = go_nn_kdtree(eps=0.1)
print("Parallel Approximate KDtree:")
print("Accuracy %lf Time %lf secs.\n"%(acc, time.time()-start_time)) 
