from bigrams import bigram_frequency
from solve import euclid, solver


with open('12.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', '')

symbols = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
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
            if not i == j:
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
    roots = solver(y1 - y2, x1 - x2, 31 * 31)
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
        if not key:
            continue
        if len(key) > 1:
            for j in key:
                if j not in keys:
                    keys.append(j)
            continue
        keys.append(key[0])
    return keys


print(len(pairs))
keys = get_keys(pairs)


def check(text):
    errors = {'ьь', 'ыы', 'аь', 'оь', 'уь', 'яь', 'юь', 'эь', 'ыы', 'оы', 'уы', 'еы', 'еь', 'эы', 'ыь', 'ьы', 'жы',
              'шы', 'щы', 'чы', 'юы', 'яы', 'аы', 'йй', 'йь', 'йы', 'фй', 'мй', 'жй', 'йх', 'пй', 'ьй'}
    length = len(text)
    i = 0
    while i < length:
        if text[i:i + 2] in errors:
            return False
        i += 2
    if text[:10] == 'аааааааааа':
        return False
    return True


def decrypt(text, key):
    result = ""
    for i in range(0, len(text) - 1, 2):
        y = get_x(text[i: i + 2])
        x = (euclid(key[0], 31 * 31)[1] * (y - key[1])) % (31 * 31)
        result += get_bigram(x)
    return result

print(len(keys))
for key in keys:
    result = decrypt(text, key)
    if check(result):
        print(result)


