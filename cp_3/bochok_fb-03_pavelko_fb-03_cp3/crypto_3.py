import codecs
import itertools
from collections import Counter

#task 1
#gsd
def gcd(a,b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

#розширений алгоритм евкліда
def evclid(a,n):
    res = [0,1]
    while n != 0 and a != 0:
        if n < a:
            res.append(a // n)
            a = a % n
        elif n > a:
            res.append(n // a)
            n = n % a
    for i in range(2, len(res) - 1):
        res[i] = res[i-2] + (-res[i]*res[i-1])
    return res[-2]

#модульне рівняння
def lin_porivnyanya(a, b, n):
    a = a % n
    b = b % n
    d = gcd(a, n)
    result = []
    if d == 1:
        x = (evclid(a, n) * b) % n
        result.append(x)
        return result
    else:
        if (b % d == 0):
            a = a // d
            b = b // d
            n = n // d
            x = (lin_porivnyanya(a,b,n)[0])
            result.append(x)
            for i in range(1, d):
                result.append(result[-1] + n)
            return result
        else:
            return result


#3 task
#функція знаходження числового індексу біграм
def ind_bi(bigram):
    temp = []
    temp.append(alphabet.index(bigram[0]))
    temp.append(alphabet.index(bigram[1]))
    ind = temp[0] * 31 + temp[1]
    return ind


#дешифратор афінного біграмного шифру
def decrypt(text, key):
    plaintext = []
    a, b = key[0], key[1]
    for i in range(0, len(text) - 1, 2):
        x = (evclid(a, 31 ** 2) * (ind_bi(text[i:i + 2]) - b)) % (31 ** 2)
        plaintext.append(alphabet[x // 31] + alphabet[x % 31])

    s = ''.join(i for i in plaintext)
    return s


#функція коммбінування теоретичних і експерементальних біграм
def combination_of_bi(topTeorBigrams, topBigrams):
    bi = []
    comb = []
    for i in topTeorBigrams:
        for j in topBigrams:
            bi.append((i, j))
    for i in bi:
        for j in bi:
            if i == j or (j, i) in comb:
                continue
            elif i[0] == j[0] or i[1] == j[1]:
                continue
            comb.append((i, j))
    return comb


#знаходження пар (a,b)[ключі]
def find_ab(combinations):
    ab = []
    x1 = ind_bi(combinations[0][0])
    x2 = ind_bi(combinations[1][0])
    y1 = ind_bi(combinations[0][1])
    y2 = ind_bi(combinations[1][1])
    a = lin_porivnyanya(x1 - x2, y1 - y2, 31 ** 2)
    for i in a:
        if gcd(i, 31) != 1:
            continue
        b = (y1 - i * x1) % 31 ** 2
        ab.append((i, b))
    return ab


#алфавіт довжиною 31
alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'

#запис файлу у змінну
with codecs.open("15.txt", "r", "utf_8_sig") as f:
    tmp_text = f.read()
text = ''.join(i for i in tmp_text if i in alphabet)


#2 task
#знаходження найчастіших біграм шифр-тексту
arr_bi = []
for i in range(0, len(text) - 1, 2):
    arr_bi.append(text[i:i + 2])
dictionary_ocr = Counter(arr_bi)
d = {key: val for key, val in sorted(dictionary_ocr.items(), key = lambda ele:ele[1], reverse=True)}
#print(d)
temp = []
for i in d:
    temp.append(i)
topBigrams = []
for i in range(0,5):
    topBigrams.append(temp[i])


#3 task
#найпопулярніші біграми заданої мови
topTeorBigrams = ["ст","но","то","на","ен"]
print(topTeorBigrams)
print(topBigrams)

#створення біграмних пар
combinations = combination_of_bi(topTeorBigrams, topBigrams)

#пошук пар (a,b)
arr_ab = []
for c in combinations:
    temp = find_ab(c)
    if len(temp) != 0:
        for j in range(len(temp)):
            arr_ab.append(temp[j])
#print(len(arr_ab))

#неможливі біграми
imposter = ['аы','оы','иы','ыы','уы','еы','аь','оь','иь','ыь','уь','еь','юы','яы','эы','юь','яь','эь', 'ць', 'хь', 'кь']
#пошук вірного ключа
key = []
for i in arr_ab:
    check = 0
    temp_txt = decrypt(text,i)
    for j in imposter:
        if j in temp_txt:
            check = 1
    if(check == 0):
        key.append(i)

#вивід ключа та розшифрованого тексту
print(key)
open_txt = decrypt(text,key[0])
print(open_txt)



