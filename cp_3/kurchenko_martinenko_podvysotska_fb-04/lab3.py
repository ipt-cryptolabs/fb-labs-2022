from collections import Counter
from itertools import product

n = 31
n2 = n ** 2
alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'

def sliser(txt):
    res = []
    for i in range(0, len(txt), 2):
        res.append(txt[i:i+2])
    return res

def most_common_bigram(txt):
    c = Counter(sliser(txt))
    return [i[0] for i in c.most_common(5)]

def bigram_to_int(bi):
    x1 = alphabet.index(bi[0])
    x2 = alphabet.index(bi[1])
    return x1 * n + x2

def int_to_bigram(num):
    f = num // n
    s = num % n
    return alphabet[f] + alphabet[s]

def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def inverted_element(a, n):
    x0, x1 = 1, 0
    while a % n:
        q = a // n
        a, n = n, a % n
        x0, x1 = x1, x0 - q * x1
    return x1

def linear(a, b, n):
    g = gcd(a, n)
    if b % g:
        return []
    a, b, n = (i // g for i in (a, b, n))
    a1 = inverted_element(a, n)
    solve = (a1 * b) % n
    return [solve + i * n for i in range(g)]

def linear_system(x1, x2, y1, y2):
    x, y = x1 - x2, y1 - y2
    solve = linear(x, y, n2)
    return [(i, (y1 - i * x1) % n2) for i in solve]

def decrypt(txt, a, b):
    answ = ''
    for i in sliser(txt):
        y = bigram_to_int(i)
        x = (inverted_element(a, n2) * (y - b)) % n2
        answ += int_to_bigram(x)
    return answ

def check(txt):
    impossible = ['аы', 'оы', 'иы', 'ыы', 'уы', 'еы', 'аь', 'оь', 'иь', 'ыь', 'уь', 'еь', 'юы', 'яы', 'эы', 'юь', 'яь', 'эь',
             'ць', 'хь', 'кь']
    for i in impossible:
        if i in txt:
            return False
    return True

with open("09.txt", 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', '')
    print(text)

reg_birgam = ['ст', 'но', 'то', 'на', 'ен']
enc_birgam = most_common_bigram(text)
print(enc_birgam)

reg_birgam = [bigram_to_int(i) for i in reg_birgam]
enc_birgam = [bigram_to_int(i) for i in enc_birgam]

keys = []


for x1, y1, x2, y2 in product(reg_birgam, enc_birgam, repeat=2):
    if x1 == x2 or y1 == y2:
        continue
    for a, b in linear_system(x1, x2, y1, y2):
        if (a, b) in keys:
            continue
        keys.append((a, b))
        decrypted = decrypt(text, a, b)
        if check(decrypted):
            print(f"""a = {a}, b = {b}
{decrypted}""")