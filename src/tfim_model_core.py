import numpy as np

def build_tfim_hamiltonian(n, lambda_1, lambda_2):
    h = np.zeros((n, n))
    delta = np.zeros((n, n))
    H = np.zeros((2*n, 2*n))

    for i in range(n):
        for j in range(n):
            if i == j:
                h[i, j] = -2
            elif abs(j - i) == 1:
                h[i, j] = lambda_1
            elif abs(j - i) == 2:
                h[i, j] = lambda_2

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

    H[:n, :n] = h
    H[:n, n:] = delta
    H[n:, :n] = -delta
    H[n:, n:] = -h

    return H
