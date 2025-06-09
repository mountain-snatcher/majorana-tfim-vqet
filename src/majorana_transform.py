import numpy as np

def build_delta(n=100, lambda_1=1.0, lambda_2=-1.2):
    delta = np.zeros((n, n), float)
    for i in range(n):
        for j in range(n):
            if j == i + 1:
                delta[i, j] = -lambda_1
            elif j == i - 1:
                delta[i, j] = lambda_1
            elif j == i + 2:
                delta[i, j] = -lambda_2
            elif j == i - 2:
                delta[i, j] = lambda_2
    return delta
