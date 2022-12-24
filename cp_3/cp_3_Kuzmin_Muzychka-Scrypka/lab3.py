import math
from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
with open('C:/Users/Gleb/Desktop/file.txt', encoding = 'utf-8') as file:
    oldfile = file.read()
newfile = ''
for letter in oldfile:
    if letter in alphabet:
        newfile += letter

def inverted_number(first, second):
    list = [0, 1]
    while first != 0 and second != 0:
        if first > second:
            list.append(first // second)
            first %= second
        else:
            list.append(second // first)
            second %= first
    for i in range(2, len(list)): 
        list[i] = list[i - 2] - list[i] * list[i - 1]
    return list[-2]

def linear_equation(a, b, n):
    x = []
    a %= n
    b %= n
    gcd = math.gcd(a, n)
    if gcd < 1:
        return x
    elif gcd == 1:
        new_elem = inverted_number(a, n) * b
        x.append(new_elem % n)
    elif gcd > 1:
        if b % gcd == 0:
            a //= gcd
            b //= gcd
            n //= gcd
            x.append((linear_equation(a, b, n)[0]))
            for i in range(1, gcd):
                x.append(x[-1] + n)
    return x

def bigram_counter():
    bigrams = []
    i = 0
    while i < len(newfile):
        bigrams.append(newfile[i:i + 2])
        i += 2
    count_bigrams = sorted(Counter(bigrams).items(), key = lambda item: item[1])
    result = []
    for i in range(5):
        result.append(list(count_bigrams[(len(count_bigrams) - (i + 1))]))
    new_result = []
    for elem in result:
        new_result.append(elem[0])
    return new_result


def possible_keys():
    finding_keys = []
    pairs = []
    chifer_bigrams = bigram_counter()
    ru_bigrams = ['ст', 'но', 'ен', 'то', 'на']
    for elem in ru_bigrams:
        for other_elem in chifer_bigrams:
            pairs.append([elem, other_elem])
    quads = []
    for elem in pairs:
        for other_elem in pairs:
            if elem == other_elem:
                continue
            elif (other_elem, elem) in pairs:
                continue
            else:
                quads.append([elem, other_elem])
    for quad in quads:
        first = alphabet.index(quad[0][0][0]) * len(alphabet) + alphabet.index(quad[0][0][1])
        second = alphabet.index(quad[1][0][0]) * len(alphabet) + alphabet.index(quad[1][0][1])
        third = alphabet.index(quad[0][1][0]) * len(alphabet) + alphabet.index(quad[0][1][1])
        fourth = alphabet.index(quad[1][1][0]) * len(alphabet) + alphabet.index(quad[1][1][1])
        key_first_part = linear_equation(first - second, third - fourth, len(alphabet) ** 2)
        for elem in key_first_part:
            if math.gcd(elem, len(alphabet)) == 1:
                key_second_part = (third - elem * first) % len(alphabet) ** 2
                if [elem, key_second_part] not in finding_keys:
                    finding_keys.append([elem, key_second_part])
    return finding_keys

def result():
    keys = possible_keys()
    for key in keys:
        decrypted_text = ''
        for i in range(0, len(newfile) - 1, 2):
            letters = (inverted_number(key[0], len(alphabet) ** 2) * (alphabet.index(newfile[i]) * len(alphabet) + alphabet.index(newfile[i + 1]) - key[1])) % (len(alphabet) ** 2)
            decrypted_text += (alphabet[letters // len(alphabet)] + alphabet[letters % len(alphabet)])
        entropy = 0
        frequency = Counter(decrypted_text)
        for elem in frequency:
            frequency[elem] = frequency[elem] / len(newfile)
            entropy -= (frequency[elem] * math.log(frequency[elem], 2))
        if 4.4 < entropy < 4.5:
            print(key)
            return decrypted_text

print(result())