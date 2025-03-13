import numpy as np


def setup(Q, T):  # pragma: no cover
    return


def sliding_dot_product(Q, T):
    m = len(Q)
    l = T.shape[0] - m + 1
    out = np.empty(l)
    for i in range(l):
        out[i] = np.dot(Q, T[i : i + m])
    return out
