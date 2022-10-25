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

text = open('pt.txt', 'r').read()
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

key_gen()
# print(keys)

def encrypt(txt: str, keys: list):
    # print(f'text len: {len(txt)}\n')
    with open('encrypted_text.txt', 'w+') as file:
        for key in keys:
            encrypted = []
            for i in range(len(txt)):
                letter = alphabet[(alphabet.index(txt[i]) + alphabet.index(key[i % len(key)]))%len(alphabet)]
                encrypted.append(letter)
            enc_txt = ''.join(encrypted)
            enc_dict = Counter(encrypted)
            index = 0
            for i in enc_dict:
                index += enc_dict[i]*(enc_dict[i] - 1)
            dict_sum = sum(enc_dict.values())
            index /= dict_sum*(dict_sum - 1)
            # print(index)
            file.write(f'key: {key}\nindex: {index}\ntext:\n{enc_txt}\n\n')
    # return 

encrypt(text, keys)


