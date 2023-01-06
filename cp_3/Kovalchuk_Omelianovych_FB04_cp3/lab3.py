import math
from collections import Counter
from textwrap import wrap
from itertools import product
alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'


def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def bigramtoint(bigram):
    a = alphabet.index(bigram[0])
    b = alphabet.index(bigram[1])
    return (a * 31 + b)

def inttobigram(number):
    return alphabet[number // 31] + alphabet[number % 31]


def decrypttext(a, b, text):
    final = ""
    a_inv = inversed_by_modulo(a, 961)
    for bigram in wrap(text, 2):
        encrypted_bigram_int = bigramtoint(bigram)
        final += inttobigram((a_inv * (encrypted_bigram_int - b)) % 961)
    return final


def inversed_by_modulo(a, m):
    a0, a1 = 1, 0
    while a % m:
        q = a // m
        a0, a1 = a1, a0 - q * a1
        a, m = m, a % m
    return a1


def count_bigrams_without_intersection_without_spaces(text):
    list0 = []

    for i in alphabet:
        for k in alphabet:
            list0.append(k + i)

    dict0 = {i:0 for i in list0}

    i = 0
    while i < len(text):
        bigram = text[i:i+2]
        dict0[bigram] += 1
        i += 2

    dictValues = list(dict0.values())
    frequencies = []
    for i in range(len(dict0)):
        frequencies.append(dictValues[i] / sum(dict0.values()))

    return {list0[i]: frequencies[i] for i in range(0, len(list0))}


def solve_a(x1x2, y1y2, n):
    gcd = math.gcd(x1x2, n)
    if gcd == 1:
        return [(inversed_by_modulo(x1x2, n) * y1y2) % n, ]
    elif y1y2 % gcd == 0:
        return ()
    x1x2 = x1x2 // gcd
    y1y2 = y1y2 // gcd
    n = n // gcd
    x = (inversed_by_modulo(x1x2, n) * y1y2) % n
    return list(x + n * i for i in range(gcd))


def solve_b(x1, x2 , y1, y2):
    x1 = bigramtoint(x1)
    x2 = bigramtoint(x2)
    y1 = bigramtoint(y1)
    y2 = bigramtoint(y2)
    a = solve_a(x1 - x2, y1 - y2, 961)
    return list([i, (y1 - i * x1) % 961] for i in a)


text = readfile("04.txt")
sorted_dict = {}
dict = count_bigrams_without_intersection_without_spaces(text)
sorted_keys = sorted(dict, key=dict.get, reverse=True)

for key in sorted_keys:
    sorted_dict[key] = dict[key]


#print(sorted_dict)
rating_of_bigrams_in_shifred_text = list(sorted_dict.keys())[0:5]
#print(rating_of_bigrams_in_shifred_text)
rating_of_bigrams_in_russian_language = ["ст", "но", "то", "на", "ен"]


def text_is_ok(text):
    if "аь" in text or "юь" in text:
        return False
    count = Counter(text)
    length = len(text)
    for i in count:
        count[i] /= length
    return count['о'] > 0.095


final_full_decrypted_text = "" 
for x1, y1, x2, y2 in product(rating_of_bigrams_in_russian_language, rating_of_bigrams_in_shifred_text, repeat=2):
    if x1 == x2 or y1 == y2:
        continue
    if len(final_full_decrypted_text) > 0:
        break
    for elem in solve_b(x1, x2, y1, y2):
        a = elem[0]
        b = elem[1]
        decrypted = decrypttext(a, b, text)
        if text_is_ok(decrypted):
            final_full_decrypted_text += decrypted
            print(a, b)
            break

print(final_full_decrypted_text)
with open('final.txt', 'w', encoding='utf-8') as f:
    f.write(final_full_decrypted_text)
