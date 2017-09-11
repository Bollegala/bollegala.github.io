import numpy

def get_union(fname):
    feats = set()
    F = open(fname)
    for line in F:
        for w in line.strip().split():
            feats.add(w)
    F.close()
    return feats

def process():
    featspace = get_union("train.positive")
    featspace = featspace.union(get_union("train.negative"))
    featspace = featspace.union(get_union("test.positive"))
    featspace = featspace.union(get_union("test.negative"))
    print len(featspace)
    pass

if __name__ == "__main__":
    process()
    