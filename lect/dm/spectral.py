import numpy as np
from numpy.linalg import norm, eig, inv


def cosine(x, y):
    return np.dot(x,y) / (norm(x) * norm(y))


def main():
    X = np.array([[1, 1, 0], [2, 2, 0], [0, 0.01, 1], [0, 0.01, 1.1]], dtype=np.float)
    print "Data Matrix"
    print X

    S = np.zeros((4,4), dtype=np.float)
    for i in range(4):
        for j in range(4):
            S[i,j] = cosine(X[i,:], X[j,:])

    print "\nSimilarity Matrix"
    print S

    D = np.zeros(4)
    for i in range(4):
        D[i] = np.sum(S[i,:])

    print "Degree matrix"
    Dm = np.diag(D)
    print Dm

    Ds = np.sqrt(inv(Dm))
    L = np.dot(Ds, np.dot(S, Ds))

    e, A = eig(L)

    print "\nEigenvalues"
    print e

    print "\nEigenvectors"
    print A

    print np.dot(L, A[:,2]) - (e[2] * A[:,2])
    pass


if __name__ == '__main__':
    main()
