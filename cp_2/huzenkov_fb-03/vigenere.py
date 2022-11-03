alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
max_key_len = 128


def encode(text, key):
    key_length = len(key)
    cypher_text = ''
    for i in range(len(text)):
        cypher_text += chr((alphabet.index(text[i]) + alphabet.index(key[i % key_length])) % len(alphabet) + 1072)
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
    for r in range(2, max_key_len):
        blocks = []
        for b in range(0, r):
            block = ''
            for j in range(b, len(cypher_text), r):
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
