import numpy

def eigen_example():
    A = numpy.random.randn(5,10)
    #A = numpy.array([[1, 2, 3], [3, 4, 7], [2, 7, 9]], dtype=numpy.float64)
    print A
    w, U = numpy.linalg.eig(A)
    L = numpy.diag(w)
    B = numpy.dot(U, numpy.dot(L, U.T))
    print B
    print "Loss =", numpy.linalg.norm(A - B)
    #P = numpy.array([[1, 2], [3, 4]])
    #Q = numpy.array([[5, 6], [7, 8]])
    #print numpy.dot(P, Q)
    pass


def svd_example(k):
    n = 10
    m = 100
    A = numpy.random.randn(n, m)
    #A = numpy.array([[1, 2, 3], [3, 4, 7], [2, 7, 9]], dtype=numpy.float64)
    #print "A =", A
    U, w, V = numpy.linalg.svd(A)
    U = U[:, :k]
    V = V[:k, :]
    L = numpy.zeros((k, k), dtype=float)
    predLoss = 0
    for i in range(k):
        #print w[i]
        L[i,i] = w[i]
    for i in range(k, n):
        predLoss += w[i] ** 2
    #print "U = ", U.shape
    #print "V = ", V.shape
    #print "L =", L.shape
    B = numpy.dot(U, numpy.dot(L, V))
    #print B
    print k, "Loss =", numpy.linalg.norm(A - B), "predLoss =", predLoss
    #P = numpy.array([[1, 2], [3, 4]])
    #Q = numpy.array([[5, 6], [7, 8]])
    #print numpy.dot(P, Q)
    pass


if __name__ == '__main__':
    #eigen_example()
    for k in range(1, 11):
        svd_example(k)