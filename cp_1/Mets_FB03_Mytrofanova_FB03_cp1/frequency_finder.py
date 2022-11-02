from collections import Counter
import csv

symbols = ' абвгдежзийклмнопрстуфхцчшщыьэюя'

with open('filtered_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
no_spaces_text = text.replace(' ', '')

letter_number = Counter(text)
no_spaces_letter_number = Counter(no_spaces_text)


def letter_frequency(dct):
    letters_frequency = {}
    letters_number = sum(dct.values())
    for letter, number in dct.items():
        letters_frequency[letter] = round(number / letters_number, 6)
    return dict(sorted(letters_frequency.items(), key=lambda x: x[1], reverse=True))


def bigram_frequency(text, no_crossing=False):
    bigrams_frequency = {}
    if no_crossing:
        step = 1
    else:
        step = 2

    for first_letter in range(0, len(text) - 1, step):
        second_letter = first_letter + 2
        if text[first_letter:second_letter] in bigrams_frequency:
            bigrams_frequency[text[first_letter:second_letter]] += 1
        else:
            bigrams_frequency[text[first_letter:second_letter]] = 0
    bigrams_number = sum(bigrams_frequency.values())

    for bigram, number in bigrams_frequency.items():
        bigrams_frequency[bigram] = round(number / bigrams_number, 6)

    return bigrams_frequency


def bigram_output(dct, spaces=True):
    bigram_matrix = []
    global symbols
    if spaces:
        alphabet = symbols
    else:
        alphabet = symbols[1:]
    for i in range(len(alphabet) + 1):
        bigram_matrix.append([0.0] * (len(alphabet) + 1))
    i, j = 1, 1
    bigram_matrix[0][0] = ' '
    for symbol in alphabet:
        bigram_matrix[i][0] = symbol
        i += 1
    for symbol in alphabet:
        bigram_matrix[0][j] = symbol
        j += 1

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            if str(alphabet[i] + alphabet[j]) in dct:
                bigram_matrix[i + 1][j + 1] = dct[str(alphabet[i] + alphabet[j])]
            elif str(alphabet[j] + alphabet[i]) in dct:
                bigram_matrix[j + 1][i + 1] = dct[str(alphabet[j] + alphabet[i])]

    return bigram_matrix


with open('letters_frequency_no_spaces.txt', 'w', encoding='utf-8') as file:
    for letter, frequency in letter_frequency(no_spaces_letter_number).items():
        file.write(str(letter) + ' - ' + str(frequency) + '\n')

with open('letters_frequency_with_spaces.txt', 'w', encoding='utf-8') as file:
    for letter, frequency in letter_frequency(letter_number).items():
        file.write(str(letter) + ' - ' + str(frequency) + '\n')

with open('bigrams_no_spaces_no_crossing.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerows(bigram_output(bigram_frequency(no_spaces_text, True), False))

with open('bigrams_spaces_no_crossing.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerows(bigram_output(bigram_frequency(text, True)))

with open('bigrams_no_spaces_crossing.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerows(bigram_output(bigram_frequency(no_spaces_text), False))

with open('bigrams_spaces_crossing.csv', 'w', encoding='utf-8') as f:
    wr = csv.writer(f)
    wr.writerows(bigram_output(bigram_frequency(text)))
