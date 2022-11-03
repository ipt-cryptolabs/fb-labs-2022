import re

import vigenere
from vigenere import *

vigenere.max_key_len = 256

text = open('text.txt', 'r').read()
text = text.lower()
text = re.sub("[^А-аЯ-я]", "", text)
index = count_index(text)
key = 'оченьсекретныйключ'
print(len(key))
cypher_text = encode(text, key)

r = count_period(cypher_text, index)
print(r)
