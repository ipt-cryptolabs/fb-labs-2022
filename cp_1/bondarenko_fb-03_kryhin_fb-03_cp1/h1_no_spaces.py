# By Bondarenko and Kryhin

from pprint import pprint
from math import log

FROM_FILE = 'text_no_spaces.txt'
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'

with open(FROM_FILE, 'r') as f:
    text = f.read().lower()
length = len(text)

letters = dict()

for i in alphabet:
    letters[i] = text.count(i)

pprint(sorted(letters.items(), key=lambda item: item[1], reverse=True), sort_dicts=False)  # sorted output

h1 = 0
for i in alphabet:
    if letters[i] == 0:
        continue
    h1 -= (letters[i] / length) * log(letters[i] / length, 2)

print(f"H1: {h1}")
