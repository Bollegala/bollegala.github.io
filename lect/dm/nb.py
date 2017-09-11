import random
import math
import sys


def count(T, fname, label):
    with open(fname) as F:
        for line in F:
            for feat in line.strip().split():
                if feat not in T:
                    T[feat] = {0:0, 1:0}
                T[feat][label] += 1
    pass


def get_vects(fname, label):
    L = []
    with open(fname) as test_file:
        for line in test_file:
            L.append((label, line.strip().split()))
    return L


def predict(T, x, pos_total, neg_total):
    pos_likelihood = neg_likelihood = 0
    for feat in x:
        print feat
        pos_likelihood += math.log(T[feat][1])
        neg_likelihood += math.log(T[feat][0])
    return 1 if pos_likelihood > neg_likelihood else 0


def naive_bayes():
    T = {}
    count(T, "train.positive", 1)
    count(T, "train.negative", 0)
    pos_total = neg_total = 0
    for feat in T:
        pos_total += T[feat][1]
        neg_total += T[feat][0]
    vocab_size = len(T)
    corrects = 0
    test_data = get_vects("test.positive", 1)
    test_data.extend(get_vects("test.negative", 0))
    random.shuffle(test_data)
    for (t, x) in test_data:
        if t == predict(x, T, pos_total, neg_total):
            corrects += 1
    print "Accuracy =", float(corrects) / float(len(test_data))
    pass

if __name__ == "__main__":
    naive_bayes()
