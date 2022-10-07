from frequency_finder import letter_frequency, bigram_frequency
from collections import Counter
import math

symbols = ' абвгдежзийклмнопрстуфхцчшщыьэюя'

with open('filtered_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
no_spaces_text = text.replace(' ', '')

letter_number = Counter(text)
no_spaces_letter_number = Counter(no_spaces_text)


def entropy(dct, n):
    entr = 0
    for freq in dct.values():
        if freq == 0:
            continue
        entr -= freq * math.log(freq, 2)
    return round(entr / n, 6)


def redundancy(entr, dct):
    return round(1 - (entr / math.log(len(dct), 2)), 6)


h1_spaces = entropy(letter_frequency(letter_number), 1)
h1_no_spaces = entropy(letter_frequency(no_spaces_letter_number), 1)
h2_spaces_crossing = entropy(bigram_frequency(text, True), 2)
h2_spaces_no_crossing = entropy(bigram_frequency(text), 2)
h2_no_spaces_crossing = entropy(bigram_frequency(no_spaces_text, True), 2)
h2_no_spaces_no_crossing = entropy(bigram_frequency(no_spaces_text), 2)
with open('results.txt', 'w', encoding='utf-8') as file:
    file.write('Letters with whitespaces entropy: ' + str(h1_spaces) + ' ; redundancy: ' + str(redundancy(h1_spaces, letter_number)) + '\n')
    file.write('Letters without whitespaces entropy: ' + str(h1_no_spaces) + ' ; redundancy: ' + str(redundancy(h1_no_spaces, no_spaces_letter_number)) + '\n')
    file.write('Bigrams with whitespaces with crossing entropy: ' + str(h2_spaces_crossing) + ' ; redundancy: ' + str(redundancy(h2_spaces_crossing, letter_number)) + '\n')
    file.write('Bigrams with whitespaces without crossing entropy: ' + str(h2_spaces_no_crossing) + ' ; redundancy: ' + str(redundancy(h2_spaces_no_crossing, letter_number)) + '\n')
    file.write('Bigrams without whitespaces with crossing entropy: ' + str(h2_no_spaces_crossing) + ' ; redundancy: ' + str(redundancy(h2_no_spaces_crossing, no_spaces_letter_number)) + '\n')
    file.write('Bigrams without whitespaces without crossing entropy: ' + str(h2_no_spaces_no_crossing) + ' ; redundancy: ' + str(redundancy(h2_no_spaces_no_crossing, no_spaces_letter_number)))