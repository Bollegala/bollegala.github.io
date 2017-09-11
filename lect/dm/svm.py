from sklearn import svm
import numpy
import sys


def get_feature_space(fname):
    A = set()
    with open(fname) as feat_file:
        for line in feat_file:
            for w in line.strip().split():
                A.add(w)
    return A


def get_feat_vects(fname, D, feat_index, label):
    feat_vects = []
    with open(fname) as feat_file:
        for line in feat_file:
            x = numpy.zeros(D, dtype=float)
            for w in line.strip().split():
                fid = feat_index[w]
                x[fid] = 1
            feat_vects.append((label,x))
    return feat_vects


def process(c):
    print "C =", c
    feat_space = get_feature_space("train.positive")
    feat_space = feat_space.union(get_feature_space("train.negative"))
    feat_space = feat_space.union(get_feature_space("test.positive"))
    feat_space = feat_space.union(get_feature_space("test.negative"))
    print "Dimensionality of the feat space =", len(feat_space)
    D = len(feat_space)
    feat_space = list(feat_space)
    feat_index = {}
    for (fid, fval) in enumerate(feat_space):
        feat_index[fval] = fid
    train_data = get_feat_vects("train.positive", D, feat_index, 1)
    train_data.extend(get_feat_vects("train.negative", D, feat_index, 0))
    test_data = get_feat_vects("test.positive", D, feat_index, 1)
    test_data.extend(get_feat_vects("test.negative", D, feat_index, 0))
    test_y = []
    train_y = []
    train_X = []
    test_X = []
    for (y, x) in train_data:
        train_X.append(x)
        train_y.append(y)
    for (y, x) in test_data:
        test_X.append(x)
        test_y.append(y)

    print "No. of train instances =", len(train_X)
    print "No. of test instances  =", len(test_X)

    clf = svm.SVC(kernel="linear", C=c)
    print "Training SVM...",
    clf.fit(train_X, train_y)
    print "Done."

    pred_y = clf.predict(test_X)
    corrects = total = 0
    for i in range(0, len(pred_y)):
        if pred_y[i] == test_y[i]:
            corrects += 1
        total += 1
    print "Accuracy =", float(100 * corrects) / float(total)
    pass

def dump_data():
    feat_space = get_feature_space("train.positive")
    feat_space = feat_space.union(get_feature_space("train.negative"))
    feat_space = feat_space.union(get_feature_space("test.positive"))
    feat_space = feat_space.union(get_feature_space("test.negative"))
    print "Dimensionality of the feat space =", len(feat_space)
    D = len(feat_space)
    feat_space = list(feat_space)
    feat_index = {}
    for (fid, fval) in enumerate(feat_space):
        feat_index[fval] = fid
    train_data = get_feat_vects("train.positive", D, feat_index, 1)
    train_data.extend(get_feat_vects("train.negative", D, feat_index, -1))
    test_data = get_feat_vects("test.positive", D, feat_index, 1)
    test_data.extend(get_feat_vects("test.negative", D, feat_index, -1))

    with open("train.txt", 'w') as F:
        for (y, x) in train_data:
            F.write("%d " % y)
            for i in range(0, D):
                if x[i] != 0:
                    F.write("%d:%f " % (i+1, x[i]))
            F.write("\n")

    with open("test.txt", 'w') as F:
        for (y, x) in test_data:
            F.write("%d " % y)
            for i in range(0, D):
                if x[i] != 0:
                    F.write("%d:%f " % (i+1, x[i]))
            F.write("\n")
    pass


if __name__ == "__main__":
    #process(float(sys.argv[1]))
    dump_data()
