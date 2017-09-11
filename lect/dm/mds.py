import numpy
import matplotlib.pyplot as plt
import sys

def bval(D, r, s):
    n = D.shape[0]
    total_r = numpy.sum(D[:,s] ** 2)
    total_s = numpy.sum(D[r,:] ** 2)
    total = numpy.sum(D ** 2)
    val = (D[r,s] ** 2) - (float(total_r) / float(n)) - (float(total_s) / float(n)) + (float(total) / float(n * n))
    return -0.5 * val

def main():
    n = 50
    m = 2
    Y = numpy.random.rand(n, m)
    D = numpy.zeros((n, n), dtype=complex)
    for i in range(0, n):
        for j in range(0, n):
            D[i, j] = numpy.exp(-0.01 * numpy.linalg.norm(Y[i] - Y[j]))
    B = numpy.zeros((n, n), dtype=complex)
    for i in range(0, n):
        for j in range(0, n):
            B[i,j] = bval(D, i, j)
    print "Distance Matrix D"
    print D
    w, V = numpy.linalg.eig(D)   
    idx = w.argsort()[::-1]
    w = w[idx]
    V = V[:,idx]
    print "\nEigenvalues of the distance matrix =", w
    print "\nB matix"
    print B
    g, U = numpy.linalg.eig(B)
    idx = g.argsort()[::-1]
    g = g[idx]
    U = U[:,idx]
    print "Eigenvalues =", g
    G = numpy.diag(numpy.sqrt(g))
    X = numpy.dot(U.T, G)
    print "\nMatrix X"
    print X
    error = 0.0
    total = 0
    for i in range(0, n):
        for j in range(i+1, n):
            error += (numpy.linalg.norm(X[i] - X[j]) - D[i, j]) ** 2
            total += 1
    RMSE = numpy.sqrt(error / float(total))
    print "RMSE =", RMSE
    if RMSE > 0:
        plt.plot(X[:,0], X[:,1], 'bo', markersize=14)
        plt.plot(Y[:,0], Y[:,1], 'ro', markersize=14)
        plt.show()
        sys.exit(1)
    pass

if __name__ == '__main__':
    while 1:
        main()




