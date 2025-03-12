X = [1, 2, 3]
P_X = [0.2, 0.5, 0.3]

def pmf(x):
    return P_X[X.index(x)] if x in X else 0

