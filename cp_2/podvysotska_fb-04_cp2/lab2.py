import re
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
m = len(alphabet) # 31

opentext = open('opentext.txt', 'r', encoding='utf-8').read().lower()

def cleanText(text):
    clean = ''
    text = text.lower().replace('ё', 'е').replace('ъ', 'ь')
    for i in text:
        if i in alphabet:
            clean += i
    return clean

opentext = cleanText(opentext)
# print(opentext)

with open('opentext.txt', 'w', encoding='utf-8') as file:
    file.write(opentext)


# 1

keys = ['юа', 'зсу', 'арта', 'гонор', 'нетмочитерпетьмуки']

def toNumbers(text):
    nums = []
    for i in range(0, len(text)):
        nums.append(alphabet.index(text[i]))
    return nums

def fromNumbers(nums):
    text = ''
    for i in range(0, len(nums)):
        text += alphabet[nums[i]]
    return text

def vigenereEncrypt(text, k):
    encrypted = []
    for i in range(len(text)):
        encrypted.append((text[i] + k[i % len(k)]) % m)
    return encrypted

encrypted_texts = []

for i in range (0, len(keys)):
    encrypted_texts.append(fromNumbers(vigenereEncrypt(toNumbers(opentext), toNumbers(keys[i]))))

print('Task 1\nEncrypted texts')
print('r = 2:')
print(encrypted_texts[0])
print('r = 3:')
print(encrypted_texts[1])
print('r = 4:')
print(encrypted_texts[2])
print('r = 5:')
print(encrypted_texts[3])
print('r = 18:')
print(encrypted_texts[4], '\n')


# 2

def coincidenceIndex(text):
    counts = Counter(text)
    coincidence = 0
    for c in counts:
        coincidence += counts[c] * (counts[c] - 1)
    coincidence /= len(text) * (len(text) - 1)
    return coincidence

coincidence_indexes = [coincidenceIndex(opentext)]

for i in range(len(encrypted_texts)):
    coincidence_indexes.append(coincidenceIndex(encrypted_texts[i]))

print('Task 2\nCoincidence indexes texts')
print('Open text: coincidence indexe =', coincidence_indexes[0])
print('r = 2: coincidence indexe =', coincidence_indexes[1])
print('r = 3: coincidence indexe =', coincidence_indexes[2])
print('r = 4: coincidence indexe =', coincidence_indexes[3])
print('r = 5: coincidence indexe =', coincidence_indexes[4])
print('r = 18: coincidence indexe =', coincidence_indexes[5], '\n')


# 3

ciphertext = open('ciphertext.txt', 'r', encoding='utf-8').read()
ciphertext = cleanText(ciphertext)

def coincidenceStatistics(text, r):
    d = 0
    for i in range(len(text) - r):
        if text[i] == text[i + r]:
            d += 1
    return d

print('Task 3\nCoincidence statistics')
D = []
for i in range(2, 32):
    D.append(coincidenceStatistics(ciphertext, i))
    print('r =', i, 'D =', D[i - 2])

period = D.index(max(D)) + 2

def getKey(text, r):
    y = []
    x = ord('о')
    for block in [text[i::r] for i in range(r)]:
        y.append(ord(Counter(block).most_common(1)[0][0]))
    k = ''
    for i in range(len(y)):
        k += alphabet[(y[i] - x) % m]
    return k

key = getKey(ciphertext, period)
print('Key =', key)

def vigenereDecrypt(text, k):
    decrypted = []
    for i in range(len(text)):
        decrypted.append((text[i] - k[i % len(k)]) % m)
    return decrypted

decrytped_text = fromNumbers(vigenereDecrypt(toNumbers(ciphertext), toNumbers(key)))
print('Decrypted text')
print(decrytped_text)