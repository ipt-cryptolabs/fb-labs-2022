import matplotlib.pyplot as plt
from collections import Counter

with open('text_for_decr.txt', 'r', encoding='utf-8') as file:
    text = file.read()
text = text.replace('\n', '')

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def find_index(text):
    index = 0
    for char in alphabet:
        index += text.count(char) * (text.count(char) - 1)
    index *= 1 / (len(text) * (len(text) - 1))
    return index


def get_blocks(text, r):
    blocks = []
    for i in range(r):
        blocks.append(text[i::r])
    return blocks


def calculate_periods(text):
    indexes = {}
    for r in range(2, 35):
        blocks = get_blocks(text, r)
        index = 0
        for block in blocks:
            index += find_index(block)
        index /= r
        indexes[r] = index
    return indexes


def find_period():
    indexes = calculate_periods(text)
    period = list(sorted(indexes.items(), key=lambda x: abs(x[1] - 0.05727))[0])[0]
    return period


def get_letters():
    letters = []
    file = open("letters_freq.txt", "r", encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        letters.append(line[0])
    file.close()
    return letters


def find_encrypted_key():
    period = find_period()
    blocks = get_blocks(text, period)
    encrypted_key = ""
    for block in blocks:
        letters_freq = Counter(block)
        encrypted_key += max(letters_freq, key=letters_freq.get)
    return encrypted_key


def decrypt_key():
    letters = get_letters()
    encrypted_key = find_encrypted_key()
    key = ''
    for char in encrypted_key:
        key += alphabet[(alphabet.find(char) - alphabet.find(letters[0])) % len(alphabet)]
    return key


# indexes = calculate_periods(text)
# print(decrypt_key())
# plt.figure(figsize=(12, 8))
# plt.bar(range(len(indexes)), list(indexes.values()), align='center')
# plt.xticks(range(len(indexes)), list(indexes.keys()))
# plt.show()


key = 'чугунныенебесачугунныенебеса'


def decrypt(text, key):
    decrypted_text = ""
    for i in range(len(text)):
        decrypted_text += alphabet[(alphabet.find(text[i]) - alphabet.find(key[i % len(key)])) % len(alphabet)]
    return decrypted_text


print(decrypt(text, key))
