# By Bondarenko and Kryhin

from pprint import pprint
from math import log

FROM_FILE = 'new_text.txt'
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя '

with open(FROM_FILE, 'r') as f:
    text = f.read().lower()

text_length = len(text)
length = text_length // 2   # determined experimentally (number of bigrams without overlap)
bigrams = dict()

for i in alphabet:
    for j in alphabet:
        bigrams[i + j] = 0

i = 0
while i < text_length:
    if i == text_length - 2:  # save from "index out of range"
        break
    bigrams[text[i:i+2]] += 1
    i += 2

pprint(sorted(bigrams.items(), key=lambda item: item[1], reverse=True), sort_dicts=False)

h2 = 0
for i in bigrams.keys():
    if bigrams[i] == 0:
        continue
    h2 -= (bigrams[i] / length) * log(bigrams[i] / length, 2)

print(f"H2: {h2 / 2}")
