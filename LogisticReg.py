#coding:utf-8
from numpy import *

def loadDataset():
    f = open("./mla/Ch05/testSet.txt")
    DataMat = []
    LabelMat = []
    for line in f.readlines():
        line_split = line.strip().split()
        DataMat.append([1.0,float(line_split[0]),float(line_split[1])])
        LabelMat.append(int(line_split[2]))
    return DataMat,LabelMat

def sigmoid(z):
    return 1.0 / (1 + exp(-z))

def LRTrain():
    DataMat,LabelMat = loadDataset()
    DataMatNP= mat(DataMat)
    LabelMatNP = mat(LabelMat).transpose()
    iter_times = 500
    alpha = 0.001
    m,n = shape(DataMatNP)
    weights = mat([1.0,1.0,1.0]).transpose()
    #weights = ones(n,1).transpose()
    for k in range(iter_times):
        sz = sigmoid(DataMatNP*weights)
        error = LabelMatNP - sz
        weights = weights + alpha*DataMatNP.transpose()*error
    return weights

def plotBestFit(weights):
    import matplotlib.pyplot as plt
    DataMat,LabelMat = loadDataset()
    x11,x10 = [],[]
    x21,x20 = [],[]
    for i in range(len(DataMat)):
        if LabelMat[i] == 1:
            x11.append(DataMat[i][1])
            x21.append(DataMat[i][2])
        else:
            x10.append(DataMat[i][1])
            x20.append(DataMat[i][2])
    x = arange(-5,5,0.1)
    y = -(weights[0,0]+ weights[1,0]*x)/weights[2,0]
    plt.plot(x11,x21,"b*",label="Class1")
    plt.plot(x10,x20,"r^",label="Class2")
    plt.plot(x,y)

    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

def plotBestFit2(weights):
    import matplotlib.pyplot as plt
    pass

def run():
    weights = LRTrain()
    print weights.getA()
    plotBestFit(weights)

def test():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0,10,1000)
    print type(x)
    y = np.sin(x)
    z = np.cos(x**2)

    plt.figure(figsize=(8,4))
    plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
    plt.plot(x,z,"b--",label="$cos(x^2)$")
    plt.xlabel("Time(s)")
    plt.ylabel("Volt")
    plt.title("PLot Example")
    plt.ylim(-1.2,1.2)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run()
