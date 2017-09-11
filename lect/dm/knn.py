"""
Task 1: Load train/test data into numpy arrays.
Task 2: Develop a k-NN classifier
"""
import numpy 


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

def similarity(z, x):
    res = numpy.dot(z,x)
    div = numpy.linalg.norm(z) * numpy.linalg.norm(x)
    return (res / div) if div != 0 else 0

def pred_knn(train_data, x, k):
    sim_scores = []
    for (l,z) in train_data:
        sim_scores.append((l, similarity(z,x)))
    sim_scores.sort(lambda x, y: -1 if x[1] > y[1] else 1)
    pos_count = neg_count = 0
    for t in sim_scores[:k]:
        if t[0] == 1:
            pos_count += 1
        else:
            neg_count += 1
    if pos_count > neg_count:
        return 1
    else:
        return -1
    pass

def process():
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
    corrects = 0
    total = 0
    for (i,(t,x)) in enumerate(test_data):
        total += 1
        pred_label = pred_knn(train_data, x, 5)
        print "%d = %d" % (i, pred_label)
        if t == pred_label:
            corrects += 1
    print "Accuracy =", float(corrects) / float(total)
    pass



if __name__ == "__main__":
    process()

    