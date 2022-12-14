from pprint import pprint
with open('02.txt', 'r', encoding='utf-8') as f:
    text = f.read().replace('\n', '')

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'

text_length = len(text)
length = text_length // 2
bigrams = dict()

for i in alphabet:
    for j in alphabet:
        bigrams[i + j] = 0

i = 0
while i < text_length:
    if i == text_length - 2:
        break
    bigrams[text[i:i+2]] += 1
    i += 2

pprint(sorted(bigrams.items(), key=lambda item: item[1], reverse=True), sort_dicts=False)
