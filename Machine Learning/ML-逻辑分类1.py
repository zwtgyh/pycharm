import numpy as np
def score(x, w, b):
    return np.dot(x, w) + b
def sigmoid(s):
    return 1. / (1 +np.exp(-s))
def softmax(s):
    return np.exp(s) / np.sum(np.exp(s), axis=0)
