def blockify(text, key_length):
    blocks = list()
    text_length = len(text)

    for i in range(key_length):
        n = i
        res = ""
        while n < text_length:
            res += text[n]
            n += key_length
        blocks.append(res)
    return blocks


def freq_max(txt):
    alphabet = {'а': 0,
                'б': 0,
                'в': 0,
                'г': 0,
                'д': 0,
                'е': 0,
                'ж': 0,
                'з': 0,
                'и': 0,
                'й': 0,
                'к': 0,
                'л': 0,
                'м': 0,
                'н': 0,
                'о': 0,
                'п': 0,
                'р': 0,
                'с': 0,
                'т': 0,
                'у': 0,
                'ф': 0,
                'х': 0,
                'ц': 0,
                'ч': 0,
                'ш': 0,
                'щ': 0,
                'ы': 0,
                'ь': 0,
                'ъ': 0,
                'э': 0,
                'ю': 0,
                'я': 0
                }

    for symbol in txt:
        alphabet[symbol] += 1
    return max(alphabet, key=alphabet.get)


def decode_key(raw_key):
    alphabet = {'а': 0,
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
                'ъ': 26,
                'ы': 27,
                'ь': 28,
                'э': 29,
                'ю': 30,
                'я': 31}
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
                    26: 'ъ',
                    27: 'ы',
                    28: 'ь',
                    29: 'э',
                    30: 'ю',
                    31: 'я'}
    freq_alphabet = "оаеинтрслвкпмудяыьзбгйчюхжшцщфэъ"
    for i in freq_alphabet:
        res = ''
        for j in raw_key:
            res += letter_codes[(alphabet[j] - alphabet[i]) % 32]
        print(res)


def main():
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read().replace("\n", '')
    key_length = 14
    raw_key = ""
    blocks = blockify(text, key_length)
    for i in blocks:
        raw_key += freq_max(i)
    print(f"raw key: {raw_key}")
    decode_key(raw_key)


if __name__ == "__main__":
    main()
