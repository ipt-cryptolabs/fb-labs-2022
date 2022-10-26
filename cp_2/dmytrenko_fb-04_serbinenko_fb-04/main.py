import random
from collections import Counter

# file = open('se.txt').read().lower().replace('\n', '').replace(' ', '').replace('ё', 'е').replace('ъ', 'ь')

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'

# txt = ''
# for i in file:
#     if i in alphabet:
#         txt += i

# print(txt)

# with open('pt.txt', 'w') as file:
#     file.write(txt)

text = open('pt.txt', 'r', encoding='utf-8').read()
var_text = open('var_text.txt', 'r', encoding='utf-8').read()
keys = []

def key_gen():
    for i in range(2, 6):
        j = 0
        key= ''
        while j < i:
            key += ''.join(random.choice(alphabet))
            j += 1
        keys.append(key)

    for i in range(10, 21):
        key= ''
        j = 0
        while j < i:
            key += ''.join(random.choice(alphabet))
            j += 1
        keys.append(key)

def encrypt(txt: str, keys: list):
    with open('encrypted_text.txt', 'w+', encoding='utf-8') as file:
        index = index_counter(txt)
        file.write(f'Our plain text\nindex: {index}\ntext:\n{txt}\n\n')
        
        for key in keys:
            encrypted = []
            for i in range(len(txt)):
                letter = alphabet[(alphabet.index(txt[i]) + alphabet.index(key[i % len(key)]))%len(alphabet)]
                encrypted.append(letter)
            enc_txt = ''.join(encrypted)
            index = index_counter(encrypted)
            file.write(f'key: {key}\nindex: {index}\ntext:\n{enc_txt}\n\n')

def index_counter(txt: str):
    plait_text = Counter(txt)
    index = 0
    for i in plait_text:
        index += plait_text[i]*(plait_text[i] - 1)
    text_sum = sum(plait_text.values())
    index /= text_sum*(text_sum - 1)
    return index

# key_gen()
# encrypt(text, keys)

def search():
    count = {}
    for i in range(1, 31):
        blocks = []
        for j in range(i):
            blocks.append(var_text[j::i])
        index = 0
        for block in blocks:
            index += index_counter(block)
        index /= i
        count[i] = index
    return count

index_dict = search()
# print(max(index_dict.values()))

key_len = max(index_dict, key=index_dict.get)
