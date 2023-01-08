from collections import Counter
from math import log2

top5 = ['ст', 'но', 'ен', 'то', 'на']

file = open('tasks/02.txt', encoding="utf-8").read().replace(' ', '').replace('\n', '')
alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
m = len(alphabet)
bigrams = []
for i in range(0,len(file),2):
    bigrams.append(file[i:i+2])
bigrams = Counter(bigrams)
text_top = []
for i in bigrams.most_common(5):
    text_top.append(i[0])
# print(text_top,)

bigrams = []
system = []
for b in top5:
    for b2 in text_top:
        bigrams.append([b, b2])
for i, b in enumerate(bigrams):
    for j, b2 in enumerate(bigrams):
        if i == j or b[0] == b2[0] or b[1] == b2[1]:
            continue
        system.append([b, b2])


new_sus=[]
for i in range(len(system)):
    a = system[i]
    ccclist = []
    for j in range(2):
        lllist = []
        for x in range(2):
            bi = a[j][x]
            num = alphabet.index(bi[0]) * 31 + alphabet.index(bi[1])
            lllist.append(num)
        ccclist.append(lllist)
    new_sus.append(ccclist)
# print(new_sus)

def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

def modular_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x

def equations(a, b, mod):
    a, b = a % mod, b % mod
    d = gcd(a, mod)
    if b % d:
        return []
    else:
        a = a // d
        b = b // d
        mod = mod // d
        x0 = modular_inverse(a, mod)
        x0 = (x0 * b) % mod
        res = [(x0 + i * mod) % mod for i in range(d)]
        return res

keys = []
for i in new_sus:
    x1, y1, x2, y2 = i[0][0], i[0][1], i[1][0], i[1][1]
    a = equations(x1 - x2, y1 - y2, m ** 2)
    for i in a:
        if gcd(i, m) != 1:
            continue
        b = (y1 - i * x1) % m ** 2
        keys.append([i, b])

def decrypt(file_txt, keys):
    text = ''
    for i in range(0, len(file_txt) - 1, 2):
        big = file_txt[i:i + 2]
        num = alphabet.index(big[0]) * 31 + alphabet.index(big[1])
        x = (modular_inverse(keys[0], 31 ** 2) * (num - keys[1])) % (31 ** 2)
        letter = alphabet[x // 31] + alphabet[x % 31]
        text += letter
    return text

new_keys =[]
while keys:
    for i in keys:
        keys.remove(i)
        new_keys.append(tuple(i))
keys = list(set(new_keys))
# print(keys)

def entropy(text): 
    countedLetters = Counter(text)
    monog = 0
    for i in countedLetters.keys():
        # print(i)
        countedLetters[i] = countedLetters[i]/len(text)
        monog += (-countedLetters[i] * log2(countedLetters[i]))
    return monog

for i in keys:
    decrypted = decrypt(file, i)
    ent = entropy(decrypted)
    if ent<4.6 and ent>4.4:
        print(f'\n\n=============== key {i} ===============\n')
        print(f'entropy is: {ent}')
        print(f'\nDecrypted text:\n{decrypted}')
        break