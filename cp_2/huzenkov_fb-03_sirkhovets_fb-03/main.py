import re
import vigenere
from vigenere import *

vigenere.max_key_len = 25

text = open('text.txt', 'r').read()
text = text.lower()
text = re.sub("[^А-аЯ-я]", "", text)
language_reference = count_frequencies(text)
index = count_index(text)
keys = ['зе', 'всу', 'воин', 'казак', 'живилюбикпи']
cyphers = []
cyphers_indexes = []
for key in keys:
    cyphers.append(encrypt(text, key))
for cypher in cyphers:
    cyphers_indexes.append(count_index(cypher))
print('Індекс відповідності відкритого тексту:', index)
for i in range(len(cyphers_indexes)):
    print('Індекс відповідності для шифротексту з ключем довжиною ', len(keys[i]), ': ', cyphers_indexes[i], sep='')

print()

variant_encrypted = open('variant.txt', 'r').read()
variant_key = find_key(variant_encrypted, count_period(variant_encrypted, index), language_reference)
variant_decrypted = decrypt(variant_encrypted, variant_key)
open('variant_decrypted.txt', 'w').write(variant_decrypted)
print('Значення ключа, обраховане алгоритмом:', variant_key)
print('Дораховане вручну значення: улановсеребряныепули')
variant_decrypted = decrypt(variant_encrypted, 'улановсеребряныепули')
open('variant_decrypted_corrected.txt', 'w').write(variant_decrypted)
