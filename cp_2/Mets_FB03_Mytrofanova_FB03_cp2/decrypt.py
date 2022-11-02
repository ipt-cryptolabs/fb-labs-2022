import matplotlib.pyplot as plt
from collections import Counter

with open('text_for_decr.txt', 'r', encoding='utf-8') as file:
    text = file.read()
text = text.replace('\n', '')

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьъэюя'


def find_index(text):
    index = 0
    for char in alphabet:
        index += text.count(char) * (text.count(char) - 1)
    index *= 1 / (len(text) * (len(text) - 1))
    return index


def get_blocks(text, r):
    blocks = []
    for i in range(r):
        iter = i
        block = ''
        while iter < len(text):
            block += text[iter]
            iter += r
        blocks.append(block)
    return blocks


def calculate_periods(text):
    indexes = {}
    for r in range(2, 35):
        blocks = get_blocks(text, r)
        index = 0
        for block in blocks:
            index += find_index(block)
        index /= len(blocks)
        indexes[r] = index
    return indexes


def find_period():
    indexes = calculate_periods(text)
    max_r = max(indexes.values())
    for key, value in indexes.items():
        if value == max_r:
            period = key
    return period


indexes = calculate_periods(text)
letters = []
file = open("letters_freq.txt", "r", encoding='utf-8')
lines = file.readlines()
for line in lines:
    letters.append(line[0])
file.close()
print(letters)



def find_key():
    period = find_period()
    blocks = get_blocks(text, period)
    key = ""
    for block in blocks:
        letters_freq = Counter(block)
        key += list(letters_freq.keys())[0]
    return key


key = find_key()
for letter in letters:
    res = ''
    for i in key:
        res += alphabet[(alphabet.find(i) - alphabet.find(letter)) % 32]
    print(res)

# plt.bar(range(len(indexes)), list(indexes.values()), align='center')
# plt.xticks(range(len(indexes)), list(indexes.keys()))
# plt.show()


