from operator import index
import re
from typing import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    return text

def write_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(text)

def vizhener_crypt(alphabet, key, text):
    shifred = ''
    values_original = []
    values_key = []
    values_shifred = []
    for letter in text:
        values_original.append(alphabet.index(letter))

    for letter in key:
        values_key.append(alphabet.index(letter))

    for value in range(len(text)):
        values_shifred.append((values_key[value % len(key)] + values_original[value]) % len(alphabet))

    for value in values_shifred:
        shifred += alphabet[value]

    return shifred

def vizhener_decrypt(text, key, alphabet):
    original_text = ''
    shifred_values = []
    key_values = []
    original_values = []

    for letter in text:
        shifred_values.append(alphabet.index(letter))

    for letter in key:
        key_values.append(alphabet.index(letter))

    for value in range(len(text)):
        original_values.append((shifred_values[value] - key_values[value % len(key)]) % len(alphabet))

    for value in original_values:
        original_text += alphabet[value]

    return original_text

def compute_index(shifr_text):
    summ = 0
    frequencies = Counter(shifr_text)
    for value in frequencies.values():
        summ += value*(value-1)

    return summ / (len(shifr_text)*(len(shifr_text) - 1))

def smash_text_into_the_blocks(text, r):
    blocks = []

    for r_ in range(0, r):
        blocks.append(text[r_])

    for koef in range(r, len(text)):
        blocks[koef % r] += text[koef]

    return blocks

text_for_crypt = readfile('text.txt')

text_for_crypt = text_for_crypt.lower()
text_for_crypt = re.sub("[^а-я]", " ", text_for_crypt)
text_for_crypt = text_for_crypt.replace("ё", "е")
text_for_crypt = text_for_crypt.replace(" ", "")

keys = ['са', 'сай', 'сайб', 'сайбе', 'сайберсекюрити']
crypted_texts = []
for key in keys:
    text = vizhener_crypt(alphabet, key, text_for_crypt)
    crypted_texts.append(text)
    write_file(key + '.txt', text)

index_for_original_text = compute_index(text_for_crypt)

print("Індекс відповідності для оригінального тексту", " : ", index_for_original_text)
for i in range(0, len(keys)):
    print(str(keys[i]), " : ", str(compute_index(crypted_texts[i])))

print("\n\n")

text_for_decrypt = readfile('shifrtext.txt')

text_for_decrypt = re.sub("[^а-я]", " ", text_for_decrypt)
text_for_decrypt = text_for_decrypt.replace(" ", "")

indexes_for_blocks = []

for i in range(2, 35):
    blocks = smash_text_into_the_blocks(text_for_decrypt, i)
    summ = 0
    for j in blocks:
        summ += compute_index(j)
    indexes_for_blocks.append(summ/i)

for i in range(0,len(indexes_for_blocks)):
    print(str(i+2) + " : " + str(indexes_for_blocks[i]))

letters_rating_by_frequency = 'оеанитлсрвкудмпьяыгзбчйжшчющэцфъ'

blocks = smash_text_into_the_blocks(text_for_decrypt, 13)


for letter in letters_rating_by_frequency[0:3]:
    kk = []
    for block in blocks:
        frequencies = Counter(block)
        dict(frequencies)
        sorted_tuple = sorted(frequencies.items(), key=lambda x: x[1], reverse = True)
        frequencies = dict(sorted_tuple)

        k = (alphabet.index(list(frequencies.keys())[0]) - alphabet.index(letter))
        kk.append(alphabet[k])
    print(kk)

final_key = 'громыковедьма'
write_file('final_deshifred_text.txt',vizhener_decrypt(text_for_decrypt, final_key, alphabet))
