import re

import vigenere
from vigenere import *

vigenere.max_key_len = 256

text = open('text.txt', 'r').read()
text = text.lower()
text = re.sub("[^А-аЯ-я]", "", text)
language_reference = count_frequencies(text)
index = count_index(text)
key = 'живилюбикпи'
print('Довжина ключа:', len(key))
cypher_text = encrypt(text, key)
r = count_period(cypher_text, index)
print('Обчислена довжина ключа:', r)
key = find_key(cypher_text, r, language_reference)
print('Знайдений ключ:', key)
