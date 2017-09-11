import math


def get_coocs(fname):
    T = {}
    N = 0
    with open(fname) as F:
        for line in F:
            N += 1
            feats = line.strip().split()[1:]
            for i in range(0, len(feats)):
                for j in range(i+1, len(feats)):
                    first = feats[i]
                    second = feats[j]
                    if first != second:
                        if (first, second) in T:
                            T[(first, second)] += 1
                        elif (second, first) in T:
                            T[(second, first)] += 1
                        else:
                            T[(first, second)] = 1
    return (T, N)


def pmi(T, totals, N):
    pmi_scores = {}
    for (first, second) in T:
        cooc_val = T[(first, second)]
        pAB = float(cooc_val) / float(N)
        pA = float(totals[first]) / float(N)
        pB = float(totals[second]) / float(N)
        pmi_scores[(first, second)] = math.log(pAB / (pA * pB))
    return pmi_scores


def get_totals(T):
    totals = {}
    for (first, second) in T:
        val = T[(first, second)]
        totals[first] = totals.get(first, 0) + val
        totals[second] = totals.get(second, 0) + val
    return totals


def main():
    T, N = get_coocs("data.txt")
    cooc_list = T.items()
    cooc_list.sort(lambda x, y: -1 if x[1] > y[1] else 1)
    k = 10
    print "Total pairs =", len(T)
    print "By cooc-freq..."
    cooc_list.reverse()
    for e in cooc_list[:k]:
        print e
    totals = get_totals(T)
    pmi_scores = pmi(T, totals, N)
    pmi_list = pmi_scores.items()
    pmi_list.sort(lambda x, y: -1 if x[1] > y[1] else 1)
    print "By PMI..."
    for e in pmi_list[:k]:
        print e
    pass

if __name__ == '__main__':
    main()
