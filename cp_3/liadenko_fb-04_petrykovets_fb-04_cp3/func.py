from collections import Counter
from textwrap import wrap
from itertools import product
import re

alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
m = 31
m_2 = 31 * 31

def clear_txt(txt: str) -> str:
    patern = '[а-яА-я]{1,}'
    res = re.findall(pattern=patern, string=txt)
    res = ''.join(res)
    res = res.lower()
    res = res.replace('ё', 'е')
    return res
# 1
def gcd(a: int, b: int) -> int:
    while a % b:
        temp = a % b
        a, b = b, temp
    return b

def reverse_a(a: int, b: int) -> int:
    u_0, u_1 = 1, 0
    while a % b:
        r = a % b
        q = a // b
        a, b = b, r
        u = u_0 - q * u_1
        u_0, u_1 = u_1, u
    return u_1

def linear_expr(a: int, b: int, n: int):
    g = gcd(a, n)
    if g == 1:
        return ((reverse_a(a, n) *b) % n,)
    if (b % g):
        return tuple()
    a //= g
    n //= g
    b //= g
    a_re = reverse_a(a, n)
    x = (a_re * b) % n
    return tuple(x + n * i for i in range(g))

# 2
def bigram_no_cross(txt: str, count: int): #без перетинів
    c = Counter(wrap(txt, 2))
    return tuple(i[0] for i in c.most_common(count))

def bigram_to_int(bi: str) -> int:
    a = alphabet.index(bi[0])
    b = alphabet.index(bi[1])
    return a * m + b

def int_to_bigram(number: int) -> str:
    a = number // m
    b = number % m
    return alphabet[a] + alphabet[b]
    
def sys_expr(x1: str, x2: str, y1: str, y2: str):
    x1, x2, y1, y2 = (bigram_to_int(numb) for numb in [x1, x2, y1, y2])
    a = linear_expr(x1 - x2, y1 - y2, m_2)
    return tuple((i, (y1 - i * x1) % m_2) for i in a)

def decrypt(txt: str, a: int, b: int) -> str:
    new = ''
    for i in wrap(txt, 2):
        y = bigram_to_int(i)
        x = (reverse_a(a, m_2) * (y - b)) % m_2
        new += int_to_bigram(x)
    return new

def encrypt(txt: str, a: int, b: int) -> str:
    new = ''
    for i in wrap(txt, 2):
        x = bigram_to_int(i)
        y = (a * x + b) % m_2
        new += int_to_bigram(y)
    return new

with open("08.txt", 'r', encoding='utf-8') as file:
    txt = file.read().replace('\n', '')

# 3

#спроба в розв'язок
def answ_big(txt: str):
    clear_bi = ('ст', 'но', 'то', 'на', 'ен')
    dirty_bi = bigram_no_cross(txt, 5)
    possible_keys = []
    for x1, y1, x2, y2 in product(clear_bi, dirty_bi, repeat=2):
        if x1 == x2 or y1 == y2:
            continue
        for a, b in sys_expr(x1, x2, y1, y2):
            if (a, b) in possible_keys:
                continue
            d = decrypt(txt, a, b)
            if bool_stuff_top(d):
                possible_keys.append((a, b))
                print(a, b, '\n', d)


# 4

def bool_stuff_top(txt: str):
    c = Counter(txt)
    _len = len(txt)
    for i in c:
        c[i] /= _len
    return c['о'] > 0.094 and c['е'] > 0.07 and c['а'] > 0.065


answ_big(txt)

a, b = 17, 94

with open('final.txt', 'w', encoding='utf-8') as f:
    f.write(decrypt(txt, a, b))