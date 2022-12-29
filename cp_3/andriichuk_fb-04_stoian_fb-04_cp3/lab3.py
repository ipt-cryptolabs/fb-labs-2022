from collections import Counter
from itertools import product
from textwrap import wrap
from math import gcd

alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
n = 31
nn = 961

def bigrams(txt: str):
    c = Counter(wrap(txt, 2)).most_common(5)
    return [i[0] for i in c]

def bigram2int(bigram):
    return alphabet.index(bigram[0]) * n + alphabet.index(bigram[1])

def int2bigram(number):
    return alphabet[number // n] + alphabet[number % n]

def inverted_by_mod(a, n):
    u0, u1 = 1, 0
    while a % n:
        q = a // n
        u0, u1 = u1, u0 - q * u1
        a, n = n, a % n
    return u1

def linear_expression_solver(a, b, n):
    """Solve expressions 'ax=b(mod n)'. Return x."""
    g = gcd(a, n)
    if g == 1:
        return [(inverted_by_mod(a, n) * b) % n]
    if b % g:
        return []
    a, b, n = map(lambda x: x % n, (a, b, n))
    answ = [(inverted_by_mod(a, n) * b) % n]
    for i in range(1, g):
        answ.append(answ[i-1] + n * i)
    return answ

def system_solver(x1, x2, y1, y2):
    """Args must be integer."""
    return [(i, (y1 - i * x1) % nn) for i in linear_expression_solver(x1 - x2, y1 - y2, nn)]

def decrypt(text, a, b):
    answ = ''
    for i in wrap(text, 2):
        y = bigram2int(i)
        x = (inverted_by_mod(a, nn) * (y - b)) % nn
        answ += int2bigram(x)
    return answ

def is_natural_text(txt):
    c = Counter(txt)
    _len = len(txt)
    for i in c:
        c[i] /= _len
    return c['ф'] < 0.003 and c['ц'] < 0.004 and c['щ'] < 0.006

with open("01.txt", 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', '')

natural_bigram = ['ст', 'но', 'то', 'на', 'ен']
encrypted_bigram = bigrams(text)
print(encrypted_bigram)

natural_bigram = [bigram2int(i) for i in natural_bigram]
encrypted_bigram = [bigram2int(i) for i in encrypted_bigram]

keys = []


for x1, y1, x2, y2 in product(natural_bigram, encrypted_bigram, repeat=2):
    if x1 == x2 or y1 == y2:
        continue
    for a, b in system_solver(x1, x2, y1, y2):
        if (a, b) in keys:
            continue
        else:
            keys.append((a, b))
        d_text = decrypt(text, a, b)
        if is_natural_text(d_text):
            print(f"""a = {a}, b = {b}
{d_text}""")

with open("decrypted.txt", 'w', encoding='utf-8') as file:
    file.write(decrypt(text, 13, 151))