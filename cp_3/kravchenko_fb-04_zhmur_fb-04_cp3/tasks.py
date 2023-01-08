from collections import Counter
from math import gcd
from textwrap import wrap
from itertools import product

alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'

p = 31
p2 = 961

def most_common_bigram(text):
    c = Counter(wrap(text, 2)).most_common(5)
    return [i[0] for i in c]

def bigram_to_int(bi):
    n1 = alphabet.index(bi[0])
    n2 = alphabet.index(bi[1])
    return n1 * p + n2

def int_to_bigram(num):
    first = alphabet[num // p]
    second = alphabet[num % p]
    return first + second

def reverse(a, n):
    a0, a1 = 1, 0
    while a % n:
        q, a, n = a // n, n, a % n
        a0, a1 = a1, a0 - q * a1
    return a1

def solve(a, b, n):
    g = gcd(a, n)
    if b % g:
        return []
    if g == 1:
        return [reverse(a, n) * b % n]
    a, b, n = [i // g for i in (a, b, n)]
    x = reverse(a, n) * b % n
    return [x + n * i for i in range(g)]

def solve_system(x1, x2, y1, y2):
    return [(i, (y1 - i * x1) % p2) for i in solve(x1 - x2, y1 - y2, p2)]

def decrypt(text, a, b):
    res = ''
    for i in wrap(text, 2):
        y = bigram_to_int(i)
        x = (reverse(a, p2) * (y - b)) % p2
        res += int_to_bigram(x)
    return res

def check(text):
    impossible = ['аы', 'оы', 'иы', 'ыы', 'уы', 'еы', 'аь', 'оь', 'иь', 'ыь', 'уь', 'еь', 
                'юы', 'яы', 'эы', 'юь', 'яь', 'эь', 'ць', 'хь', 'кь']
    for i in impossible:
        if i in text:
            return False
    return True

with open('03.txt', 'r', encoding='utf-8') as f:
    text = f.read().replace('\n', '')

natural = ['ст', 'но', 'то', 'на', 'ен']
encrypted = most_common_bigram(text)
print(encrypted)

natural = [bigram_to_int(i) for i in natural]
encrypted = [bigram_to_int(i) for i in encrypted]
done = False

for x1, y1, x2, y2 in product(natural, encrypted, repeat=2):
    if x1 == x2 or y1 == y2:
        continue
    for a, b in solve_system(x1, x2, y1, y2):
        dtext = decrypt(text, a, b)
        if check(dtext):
            print(a, b, dtext)
            done = True
    if done:
        break
