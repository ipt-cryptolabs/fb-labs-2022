import re
from itertools import permutations
from collections import Counter


def euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = euclidean_algorithm(b, a % b)
        return gcd, y, x - y * (a // b)


def linear(a, b, m):
    gcd, a1, y = euclidean_algorithm(a, m)
    result = []
    if gcd == 1:
        if ((a * a1) % m) == 1:
            result.append((a1 * b) % m)
            return result
    else:
        if b % gcd != 0:
            return
        else:
            gcd, q, a1 = euclidean_algorithm(a, m)
            for i in range(gcd - 1):
                x = (a1 * b) % m + i * m
                result.append(x)
            return result


def bigram_counts(txt):
    bigram_c = Counter([txt[i: i + 2] for i in range(0, len(txt), 2)])
    return [bigram[0] for bigram in bigram_c.most_common(5)]


def bigram_index(bigram, alpha):
    return alpha.index(bigram[0]) * (len(alpha)) + alpha.index(bigram[1])


def filter(text, alpha):
    return re.sub(f"[^{alpha}]", "", text)


def bigram_analyze(freq, bigram):
    perm = permutations(freq)
    result = []
    for p in perm:
        comb = {}
        for i in range(len(bigram)):
            comb[bigram[i]] = p[i]
        result.append(comb)
    return result

def bigram_xy(bigram_, bigram, alpha):
    Xs = []
    Ys = []
    for num in bigram:
        Xs.append(bigram_index(num, alpha))
    for num in bigram_:
        Ys.append(bigram_index(num, alpha))
    #print(Xs,Ys)
    return Xs, Ys

def key_search(bigram, alpha):
    x1, y1, x2, y2 = bigram[0][1], bigram[0][0], bigram[1][1], bigram[1][0] 
    N = len(alpha)
    a = linear(x1 - x2, y1 - y2, N**2)
    if not a is None:
        b = [(y1 - (x1 * a[elements])) % N**2 for elements in range(len(a))]
        return (a[0], b[0])
    return


def decrypt(a, b, m, text, test_keys, alpha):
    N = len(text)
    result = []
    gcd, a_, q = euclidean_algorithm(a, m)
    if N % 2 == 1: 
        N -= 1
    for bi in [text[i:i + 2] for i in range(0, N, 2)]:
        y = bigram_index(bi, alpha)
        x = (y - b) * a_ % m
        x2 = x % 31
        x1 = ((x - x2) // 31) % 31
        bigram = alpha[x1] + alpha[x2]
        if bigram not in ['аь', 'еь', 'жы', 'уь', 'фщ', 'хы', 'хь', 'цщ', 'цю', 'чф', 'чц', 'чщ', 'шы', 'щы', 'ыь', 'ьы', 'эы', 'эь', 'юы', 'юь', 'яы', 'яь', 'ьь']:
            if a != 0: result.append(bigram)
        else:
            result.clear()
            return test_keys, result

    if len(result) > 0:
        result = ''.join(result)
        test_keys.append((a, b))
    return test_keys, result
