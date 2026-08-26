import numpy as np


def genrate_linear_data(n = 100):
    X = np.random.randn(n, 2)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    return X, y

def generate_non_linear_data(n=100, noise=0.1):
    radius = np.random.rand(n)
    angle = 2 * np.pi * np.random.rand(n)

    x1 = radius * np.cos(angle) 
    x2 = radius * np.sin(angle) 

    X = np.column_stack((x1, x2))
    y = (radius > 0.5).astype(int)

    X += noise + np.random.randn(n, 2)
    return X, y

