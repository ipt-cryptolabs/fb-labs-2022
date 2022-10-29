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

def vizhener(alphabet, key, text):
    shifred = ''
    values_original = []
    values_key = []
    values_shifred = []
    for i in text:
        values_original.append(alphabet.index(i))

    for i in key:
        values_key.append(alphabet.index(i))

    for i in range(len(text)):
        values_shifred.append((values_key[i % len(key)] + values_original[i]) % len(alphabet))

    for i in values_shifred:
        shifred += alphabet[i]

    return shifred

def vizhener_deshifr(text, key, alphabet):
    original_text = ''
    shifred_values = []
    key_values = []
    original_values = []

    for i in text:
        shifred_values.append(alphabet.index(i))

    for i in key:
        key_values.append(alphabet.index(i))

    for i in range(len(text)):
        original_values.append((shifred_values[i] - key_values[i % len(key)]) % len(alphabet))

    for i in original_values:
        original_text += alphabet[i]

    return original_text

def compute_indexes(shifr_text):
    summ = 0
    N = Counter(shifr_text)
    for i in N.values():
        summ += i*(i-1)

    return summ / (len(shifr_text)*(len(shifr_text) - 1))

text_to_shifr = readfile('text.txt')

text_to_shifr = text_to_shifr.lower()
text_to_shifr = re.sub("[^а-я]", " ", text_to_shifr)
text_to_shifr = text_to_shifr.replace("ё", "е")
text_to_shifr = text_to_shifr.replace(" ", "")

print(text_to_shifr)

keys = ['са', 'сай', 'сайб', 'сайбе', 'сайберсекюрити']
shifred_texts = []
for i in keys:
    text = vizhener(alphabet, i, text_to_shifr)
    shifred_texts.append(text)
    write_file(i + '.txt', text)



index_for_original_text = compute_indexes(text_to_shifr)
print(index_for_original_text)
for i in shifred_texts:
    print(compute_indexes(i))

print(1/len(alphabet))

print("\n\n\n\n\n")

text_to_deshifr = readfile('shifrtext.txt')

text_to_deshifr = re.sub("[^а-я]", " ", text_to_deshifr)
text_to_deshifr = text_to_deshifr.replace(" ", "")

arr = []

def smash_text_into_the_blocks(text, r):
    blocks = []

    for r_ in range(0, r):
        blocks.append(text[r_])

    for koef in range(r, len(text)):
        blocks[koef % r] += text[koef]

    return blocks


for i in range(2, 35):
    blocks = smash_text_into_the_blocks(text_to_deshifr, i)
    summ = 0
    for j in blocks:
        summ += compute_indexes(j)
    arr.append(summ/i)

arr_new = []

for i in range(0,len(arr)):
    print(str(i+2) + ":" + str(arr[i]))

rating_bukv = 'оеанитлсрвкудмпьяыгзбчйжшчющэцфъ'

blocks = smash_text_into_the_blocks(text_to_deshifr, 13)

keys = []

for block in blocks:
    count = Counter(block)
    dict(count)
    sorted_tuple = sorted(count.items(), key=lambda x: x[1], reverse = True)
    count = dict(sorted_tuple)
    k = (alphabet.index(list(count.keys())[0]) - alphabet.index(rating_bukv[0]))
    keys.append(k)

mystr = ''

for i in keys:
    mystr += alphabet[i]

print(mystr)

print(vizhener_deshifr(text_to_deshifr, mystr, alphabet))