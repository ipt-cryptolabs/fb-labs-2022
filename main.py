from collections import Counter
from itertools import permutations
from math import log2

alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
most_frequency_bigrams = 'ст', 'но', 'то', 'на', 'ен'
modulus = len(alphabet)

cipher_text = open("var8_dvornikov.txt", "r", encoding="utf-8").read().replace("\n", "")


def euclid(a: float, b: float) -> [float]:
    x0, x1 = 1, 0

    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
    return a, x0


def find_inverse(a: int or float, b: int or float) -> [float, None or float]:
    d, x = euclid(a, b)
    if d == 1:
        return d, x % b
    return d, None


def converter(bigram: list) -> float:
    return alphabet.find(bigram[0]) * 31 + alphabet.find(bigram[1])


def entropy(text: dict, s_len: int, n=1) -> float:
    entropy_dict = {}
    for letter in text:
        entropy_dict[letter] = text[letter] / s_len * log2(text[letter] / s_len)
    return -sum(entropy_dict.values()) / n


def counter(text: str, step: int, sort=True) -> list or str:
    bigrams_count = Counter([text[i:i + 2] for i in range(0, len(text) - 1, step)])
    return sorted(bigrams_count.items(), key=lambda x: x[1], reverse=True) if sort else bigrams_count


def solve_linear_comparison(a: float, b: float, mod: float) -> list:
    d, inverse = find_inverse(a, mod)
    if inverse:
        return [(inverse * b) % mod]
    if not b % d:
        return [int((b / d * find_inverse(a / d, mod / d)[1]) % mod / d + (i - 1) * mod / d) for i in range(1, d + 1)]


def find_fisrt(x1: str, x2: str, y1: str, y2: str) -> [list[int], None]:
    params = [alphabet.index(y1[0]) * modulus + alphabet.index(y1[1]),
              alphabet.index(y2[0]) * modulus + alphabet.index(y2[1]),
              alphabet.index(x1[0]) * modulus + alphabet.index(x1[1]),
              alphabet.index(x2[0]) * modulus + alphabet.index(x2[1])]

    results = solve_linear_comparison(params[0] - params[1], params[2] - params[3], modulus * modulus)
    if results is not None:
        fisrt_keys = [find_inverse(i, modulus * modulus)[1] for i in results]
        return [x for x in fisrt_keys if x is not None]


def find_second(x1: str, y1: str, a: [list]) -> int:
    params = [alphabet.index(y1[0]) * len(alphabet) + alphabet.index(y1[1]),
              alphabet.index(x1[0]) * len(alphabet) + alphabet.index(x1[1])]
    return (params[0] - a * params[1]) % len(alphabet) ** 2


def check_text_correctness(symbols: dict, bigrams: dict, text_length: int) -> bool:
    return entropy(bigrams, text_length, n=2) < 4.2 and entropy(symbols, text_length) < 4.5


def decrypt_affine(text: str, key: tuple[int, int]) -> str:
    mod = modulus * modulus
    decrypt_text = ''
    for i in range(0, len(text), 2):
        a_inverse = find_inverse(key[0], mod)[1]
        Y_b = (alphabet.index(text[i]) * modulus + alphabet.index(text[i + 1]) - key[1])
        ans = (a_inverse * Y_b) % mod
        decrypt_text += alphabet[ans // modulus] + alphabet[ans % modulus]
    return decrypt_text


def find_keys(cipher_text: str) -> (str,str):
    most_bigrams = counter(cipher_text, 1)[:5]
    for i in permutations(most_frequency_bigrams, 2):
        for j in range(4):
            predicted_key = find_fisrt(i[0], i[1], most_bigrams[j][0], most_bigrams[j + 1][0])
            if predicted_key is None:
                continue
            for solution in predicted_key:
                key = solution, find_second(i[0], most_bigrams[j][0], solution)
                if check_text_correctness(Counter(decrypt_affine(cipher_text, key)),
                                          counter(decrypt_affine(cipher_text, key), 1, sort=False),
                                          len(decrypt_affine(cipher_text, key))):
                    return key,decrypt_affine(cipher_text, key)
