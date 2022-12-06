from math_solve import equation_solver, inverse_element


MOD = 31
letter_codes = {0: 'а',
                1: 'б',
                2: 'в',
                3: 'г',
                4: 'д',
                5: 'е',
                6: 'ж',
                7: 'з',
                8: 'и',
                9: 'й',
                10: 'к',
                11: 'л',
                12: 'м',
                13: 'н',
                14: 'о',
                15: 'п',
                16: 'р',
                17: 'с',
                18: 'т',
                19: 'у',
                20: 'ф',
                21: 'х',
                22: 'ц',
                23: 'ч',
                24: 'ш',
                25: 'щ',
                26: 'ь',
                27: 'ы',
                28: 'э',
                29: 'ю',
                30: 'я'}
alphabet = {
        'а': 0,
        'б': 1,
        'в': 2,
        'г': 3,
        'д': 4,
        'е': 5,
        'ж': 6,
        'з': 7,
        'и': 8,
        'й': 9,
        'к': 10,
        'л': 11,
        'м': 12,
        'н': 13,
        'о': 14,
        'п': 15,
        'р': 16,
        'с': 17,
        'т': 18,
        'у': 19,
        'ф': 20,
        'х': 21,
        'ц': 22,
        'ч': 23,
        'ш': 24,
        'щ': 25,
        'ь': 26,
        'ы': 27,
        'э': 28,
        'ю': 29,
        'я': 30
    }


def is_text(text: str) -> bool:
    errors = {'ьь', 'ыы', 'аь', 'оь', 'уь', 'яь', 'юь', 'эь', 'ыы', 'оы', 'уы', 'еы', 'еь', 'эы', 'ыь', 'ьы', 'жы',
              'шы', 'щы', 'чы', 'юы', 'яы', 'аы', 'йй', 'йь', 'йы', 'фй', 'мй', 'жй', 'йх', 'пй', 'ьй'}
    length = len(text)
    i = 0
    while i < length:
        if text[i:i+2] in errors:
            return False
        i += 2
    if text[:10] == 'аааааааааа':
        return False
    return True


def make_pairs(llist: list, rlist: list) -> list:
    bigram_pairs = list()
    pairs = list()
    for i in rlist:
        for j in llist:
            bigram_pairs.append((i, j))

    for i in bigram_pairs:
        for j in bigram_pairs:
            pairs.append((i, j))
    return pairs


def bigram2int(bigram: str, mod: int) -> int:
    return alphabet[bigram[0]] * mod + alphabet[bigram[1]]


def int2bigram(val, mod: int) -> str:
    second = val % mod
    first = (val - second) // mod
    return letter_codes[first] + letter_codes[second]


def system_solve(pair: tuple) -> list:
    result = list()
    x1 = bigram2int(pair[0][0], MOD)
    x2 = bigram2int(pair[1][0], MOD)
    y1 = bigram2int(pair[0][1], MOD)
    y2 = bigram2int(pair[1][1], MOD)
    a = equation_solver(y1 - y2, x1 - x2, MOD ** 2)
    if a is None:
        return result
    for i in a:
        result.append((i, (y1 - i * x1) % (MOD ** 2)))

    return result


def decipher(text: str, key: tuple) -> str:
    n = 0
    length = len(text)
    result = ""
    while n < length:
        y = bigram2int(text[n:n + 2], MOD)
        x = (inverse_element(key[0], MOD ** 2) * (y - key[1])) % (MOD ** 2)
        result += int2bigram(x, MOD)
        n += 2
    return result


def main():
    with open('02.txt', 'r', encoding='utf-8') as f:
        txt = f.read().replace('\n', '')

    pairs = make_pairs(
        ['йа', 'юа', 'чш', 'юд', 'рщ'],
        ['ст', 'но', 'то', 'на', 'ен'])

    keys = list()
    for i in pairs:
        key = system_solve(i)
        if len(key) == 0:
            continue
        if len(key) > 1:
            for j in key:
                if j not in keys:
                    keys.append(j)
            continue
        keys.append(key[0])

    for i in keys:
        dec = decipher(txt, i)
        if is_text(dec) is True:
            print(f"key: {i}")
            print(dec)
            with open('plaintext.txt', 'w', encoding='utf-8') as f:
                f.write(dec)


if __name__ == "__main__":
    main()
