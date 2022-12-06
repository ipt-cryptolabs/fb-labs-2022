# By Bondarenko and Kryhin

from pprint import pprint
from math import log

FROM_FILE = 'new_text.txt'
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя '

with open(FROM_FILE, 'r') as f:
    text = f.read().lower()

length = len(text) - 1  # determined experimentally (number of bigrams)
bigrams = dict()  # numbers of each bigram

for i in alphabet:
    for j in alphabet:
        bigrams[i + j] = 0

for i in bigrams.keys():
    bigrams[i] = text.count(i)

pprint(sorted(bigrams.items(), key=lambda item: item[1], reverse=True), sort_dicts=False)  # sorted output

h2 = 0
for i in bigrams:
    if bigrams[i] == 0:
        continue
    h2 -= (bigrams[i] / length) * log(bigrams[i] / length, 2)

print(f"H2: {h2 / 2}")
