import multiprocessing as mp
from sklearn.datasets import load_svmlight_file
import numpy as np
import time

from numba import jit

traindata = load_svmlight_file("a9a.subset.train")
testdata = load_svmlight_file("a9a.subset.test")
Xtrain = traindata[0].todense()
ytrain = traindata[1]
Xtest = testdata[0].todense()
ytest = testdata[1]

@jit(nopython=True)
def go_nn(Xtrain, ytrain, Xtest, ytest):
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


start_time = time.time()
acc = go_nn(Xtrain, ytrain, Xtest, ytest)
print("Accuracy %lf Time %lf secs.\n"%(acc, time.time()-start_time)) 
