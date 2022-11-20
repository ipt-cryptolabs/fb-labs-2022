from bigrams import bigram_frequency
from solve import euclid, solver

with open('12.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', '')

symbols = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
encrypted_bigrams = list(bigram_frequency(text).keys())[:5]
freq_bigrams = ['ст', 'но', 'то', 'на', 'ен']


def create_pairs(b1, b2):
    bigrams = []
    pairs = []
    for normal in b1:
        for encrypted in b2:
            bigrams.append((normal, encrypted))
    for i in bigrams:
        for j in bigrams:
            if not i == j and not (j, i) in pairs and i[0] != j[0] and i[1] != j[1]:
                pairs.append((i, j))
    return pairs


pairs = create_pairs(freq_bigrams, encrypted_bigrams)


def get_x(bigram):
    return symbols.index(bigram[0]) * 31 + symbols.index(bigram[1])


def get_bigram(value):
    return symbols[value // 31] + symbols[value % 31]


def find_key(pair):
    x1, y1 = get_x(pair[0][0]), get_x(pair[0][1])
    x2, y2 = get_x(pair[1][0]), get_x(pair[1][1])
    roots = solver(x1 - x2, y1 - y2, 31 * 31)
    if roots is None:
        return None
    key = []
    for a in roots:
        key.append((a, (y1 - a * x1) % (31 * 31)))
    return key


def get_keys(pairs):
    keys = []
    for pair in pairs:
        key = find_key(pair)
        if key:
            for k in key:
                keys.append(k)
    return keys


keys = get_keys(pairs)


def decrypt(text, key):
    result = ""
    for i in range(0, len(text) - 1, 2):
        y = get_x(text[i: i + 2])
        x = (euclid(key[0], 31 * 31)[1] * (y - key[1])) % (31 * 31)
        result += get_bigram(x)
    return result


def check(text, keys):
    wrong = ['аы', 'оы', 'иы', 'ыы', 'уы', 'еы', 'аь', 'оь', 'иь', 'ыь', 'уь', 'еь', 'юы', 'яы', 'эы', 'юь', 'яь', 'эь',
             'ць', 'хь', 'кь']
    valid = True
    for key in keys:
        result = decrypt(text, key)
        for bigram in wrong:
            if bigram in result:
                valid = False
        if valid:
            print(key)
            print(result)
            return
        valid = True


check(text, keys)
