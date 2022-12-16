import euclidean

ALPHA = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']


def bigrams_probability(text, step=1):  # taken from lab 1
    bigrams_dict = {}
    for i in range(0, len(text) - 1, step):
        j = i + 2
        if text[i:j] in bigrams_dict:
            bigrams_dict[text[i:j]] += 1
        else:
            bigrams_dict[text[i:j]] = 1
    bigrams_dict2 = []
    for i in bigrams_dict:
        bigrams_dict2.append((i, bigrams_dict[i]))
    return sorted(bigrams_dict2, key=lambda x: x[1], reverse=True)


def biagram_number(biagram):
    return ALPHA.index(biagram[0]) * len(ALPHA) + ALPHA.index(biagram[1])


def get_key(coded_biagrams, biagrams):
    y_ = biagram_number(coded_biagrams[0]) - biagram_number(coded_biagrams[1])
    x_ = biagram_number(biagrams[0]) - biagram_number(biagrams[1])
    keys = euclidean.linear_comparison(x_, y_, len(ALPHA) ** 2)
    ans = []
    if keys is not None:
        if len(keys) > 0:
            for i in keys:
                ans.append((i, (biagram_number(coded_biagrams[0]) -
                    i * biagram_number(biagrams[0])) % (len(ALPHA) ** 2)))
        return ans


def number_biagram(number):
    second = number % len(ALPHA)
    first = number // len(ALPHA)
    return ALPHA[first] + ALPHA[second]


def decryption(text, key):
    n = 0
    result = ""
    while n < len(text):
        y = biagram_number(text[n: n + 2])
        x = (euclidean.articled_element(key[0], len(ALPHA) ** 2) * (y - key[1])) % (len(ALPHA) ** 2)
        result += number_biagram(x)
        n += 2
    return result


def is_here_good_one(text, keys):
    errors = ['еь', 'юы', 'яы', 'аы', 'оы', 'иы' 'аь', 'оь', 'ыь', 'уь', 'эы', 'ыы', 'уы', 'еы', 'юь', 'яь', 'эь',
              'ць']
    good_one = True
    for key in keys:
        result = decryption(text, key)
        for eror in errors:
            if eror in result:
                good_one = False
        if good_one:
            return key, result
        good_one = True


if __name__ == '__main__':

    with open('03.txt', 'r', encoding='UTF-8') as f:
        text = f.read().replace('\n', '')

    top_encrypted = bigrams_probability(text, 2)[:5]

    top_5 = ['ст', 'но', 'то', 'на', 'ен']

    pair_set = []
    for i in top_encrypted:
        for j in top_5:
            pair_set.append((j, i[0]))
    compliance = []
    for i in pair_set:
        for j in pair_set:
            if not i == j and not (j, i) in compliance and i[0] != j[0] and i[1] != j[1]:
                compliance.append((i, j))

    keys = []
    for i in compliance:
        answer_keys = get_key((i[0][1], i[1][1]), (i[0][0], i[1][0]))
        if answer_keys is None:
            continue
        for k in answer_keys:
            keys.append(k)

    victory = is_here_good_one(text, keys)
    print(f"Our key: {victory[0]}")
    print(f"Decrypted text: {victory[1]}")

    with open('answer.txt', 'w') as f:
        f.write(victory[1])
