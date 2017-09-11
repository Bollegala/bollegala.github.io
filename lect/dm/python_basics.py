import math

def get_vector(s):
    words = s.split()
    v = {}
    for w in words:
        v[w] = v.get(w, 0) + 1
    return v


def cos(x, y):
    total = 0
    for word in x:
        total += x[word] ** 2
    x_norm = math.sqrt(total)

    total = 0
    for word in y:
        total += y[word] ** 2
    y_norm = math.sqrt(total)

    overalp = 0
    for word in x:
        if word in y:
            overalp += x[word] * y[word]

    res = overalp / (x_norm * y_norm)
    return res



def main():
    L = [(1, "this is very exiting"), \
            (-1, "boring movie. never watch again"), \
            (1, "good animations"), \
            (-1, "too crowded bad choice")]
    fv = []
    for (label, txt) in L:
        fv.append((label, get_vector(txt)))

    test = "this is a good movie"
    test_vect = get_vector(test)

    for (label, v) in fv:
        print label, cos(v, test_vect)

    F = open("myfile.txt")
    txt = F.read()
    F.close()
    print txt

    print fv


if __name__ == "__main__":
    main()
