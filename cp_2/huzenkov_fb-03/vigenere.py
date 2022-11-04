from copy import deepcopy
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
max_key_len = 128


def encrypt(text, key):
    key_length = len(key)
    cypher_text = ''
    for i in range(len(text)):
        cypher_text += chr((alphabet.index(text[i]) + alphabet.index(key[i % key_length])) % len(alphabet) + 1072)
    return cypher_text


def decrypt(text, key):
    key_length = len(key)
    cypher_text = ''
    for i in range(len(text)):
        cypher_text += chr((alphabet.index(text[i]) - alphabet.index(key[i % key_length])) % len(alphabet) + 1072)
    return cypher_text


def count_frequencies(text):
    freq = dict()
    for i in text:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq


def count_index(text):
    text_len = len(text)
    sum_of_frequencies = 0
    freqs = count_frequencies(text)
    for i in freqs:
        sum_of_frequencies += freqs[i] * (freqs[i] - 1)
    index = sum_of_frequencies/(text_len * (text_len - 1))
    return index


def count_period(cypher_text, theoretical_index):
    indexes = []
    differences = []
    ct_len = len(cypher_text)
    for r in range(2, max_key_len):
        blocks = []
        for b in range(0, r):
            block = ''
            for j in range(b, ct_len, r):
                block += cypher_text[j]
            blocks.append(block)
        period_indexes = []
        for b in blocks:
            period_indexes.append(count_index(b))
        # sum_indexes /= len(blocks)
        indexes.append(min(period_indexes))
    for i in indexes:
        differences.append(abs(theoretical_index - i))
    return differences.index(min(differences)) + 2


def find_caesar_key(cypher_text, language_reference):
    frequencies = count_frequencies(cypher_text)
    keys = ''
    for i in range(len(alphabet)-1):
        reference_most_frequent = ''
        cypher_text_most_frequent = ''
        max = 0
        for key, value in language_reference.items():
            if value > max:
                reference_most_frequent = key
                max = value
        max = 0
        for key, value in frequencies.items():
            if value > max:
                cypher_text_most_frequent = key
                max = value
        keys += chr(abs(alphabet.index(reference_most_frequent) - alphabet.index(cypher_text_most_frequent)) % len(alphabet) + 1072)
        frequencies.pop(cypher_text_most_frequent)
        language_reference.pop(reference_most_frequent)
    keys = count_frequencies(keys)
    key = ''
    max = 0
    for k, v in keys.items():
        if v > max:
            key = k
            max = v
    return key


def find_key(cypher_text, key_length, language_reference):
    ct_len = len(cypher_text)
    key = ''
    blocks = []
    for i in range(key_length):
        block = ''
        for j in range(i, ct_len, key_length):
            block += cypher_text[j]
        blocks.append(block)
    for b in blocks:
        key += find_caesar_key(b, deepcopy(language_reference))
    return key
