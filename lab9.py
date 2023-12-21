import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def kernel(point, xmat, k):
    m = np.shape(xmat)[0]
    weights = np.mat(np.eye(m))
    for i in range(m):
        diff = point - xmat[i]
        weights[i, i] = np.exp(diff * diff.T / (-2.0 * k ** 2))
    return weights

def localWeight(point, xmat, ymat, k):
    wei = kernel(point, xmat, k)
    return (xmat.T * (wei * xmat)).I * (xmat.T * (wei * ymat.T))

def localWeightRegression(xmat, ymat, k):
    m = np.shape(xmat)[0]
    ypred = np.zeros(m)
    for i in range(m):
        ypred[i] = xmat[i] * localWeight(xmat[i], xmat, ymat, k)
    return ypred

def graphPlot(X, ypred):
    index = X[:, 1].argsort(0)
    xsort = X[index][:, 0][:, 1]
    plt.scatter(bill, tip, color='green')
    plt.plot(xsort, ypred[index], color='red', linewidth=5)
    plt.xlabel('Total bill')
    plt.ylabel('Tip')
    plt.show()

data = pd.read_csv('datasets/9.csv')

bill, tip = np.array(data.total_bill), np.array(data.tip)
mbill, mtip = np.mat(bill), np.mat(tip)

X = np.column_stack((np.ones(mbill.shape[1]), mbill.T))
ypred = localWeightRegression(X, mtip, 5)
graphPlot(X, ypred)