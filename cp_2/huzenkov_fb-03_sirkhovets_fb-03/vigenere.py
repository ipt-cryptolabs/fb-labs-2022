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
        if i not in freq.keys():
            freq[i] = 1
        else:
            freq[i] += 1
    return freq


def count_index(text):
    text_len = len(text)
    sum_of_frequencies = 0
    frequencies = count_frequencies(text)
    for i in frequencies:
        sum_of_frequencies += frequencies[i] * (frequencies[i] - 1)
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


def most_common(frequency_table):
    most_frequent = ''
    frequency = -1
    for key, value in frequency_table.items():
        if value > frequency:
            frequency = value
            most_frequent = key
    return most_frequent


def find_caesar_key(cypher_text, reference_most_frequent):
    frequencies = count_frequencies(cypher_text)
    cypher_most_frequent = most_common(frequencies)
    key = chr((alphabet.index(cypher_most_frequent) - alphabet.index(reference_most_frequent)) % len(alphabet) + 1072)
    return key


def find_key(cypher_text, key_length, language_reference):
    ct_len = len(cypher_text)
    key = ''
    blocks = []
    for i in range(0, key_length):
        block = ''
        for j in range(i, ct_len, key_length):
            block += cypher_text[j]
        blocks.append(block)
    most_frequent = most_common(language_reference)
    for b in blocks:
        key += find_caesar_key(b, most_frequent)
    return key
