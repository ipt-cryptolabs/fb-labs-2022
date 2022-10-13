from collections import Counter
from math import log2

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя '
text = open('../texts/Унесенные ветром. Маргарет Митчелл.txt', "r").read().lower().replace('ё', "е").replace("ъ", "ь")

ru_txt = ''
for i in text:
    if i in alphabet:
        ru_txt += i

text_space = ''
space = 0
for i in ru_txt:
    if i == ' ':
        if space != 0:
            pass
        else:
            text_space += i
        space += 1
    else:
        text_space += i
        space = 0

text_no_space = text_space.replace(' ', '')

open('../texts/text_space.txt', 'w').write(text_space)
open('../texts/text_no_space.txt', 'w').write(text_no_space)

def count_letters(dict):
    count = 0
    for key in dict.keys():
        count += dict[key]
    return count

def freq(dict, text_len):
    for key in dict.keys():
        dict[key] = dict[key]/text_len
    return dict

def bigrams_counter(text, is_crossed=True):
    if is_crossed == True:
        lst_bigrmas = [text[i:i + 2] for i in range(0, len(text) - 1)]
    else:
        lst_bigrmas = [text[i:i + 2] for i in range(0, len(text) - 1, 2)]
    bigrams = Counter(lst_bigrmas)
    return bigrams

def entropy(dict, isMono=False):
    e = 0
    for key in dict:
        e += -(dict[key] * log2(dict[key]))
    if isMono == True:
        pass
    else:
        e = e * 1 / 2
    return e

def calc_R(ent, space=True):
    if space == True:
        return 1 - ent / log2(32)
    else:
        return 1 - ent / log2(31)

monogram_space = dict(sorted(freq(Counter(text_space), count_letters(Counter(text_space))).items(), key=lambda item: item[1], reverse=True))
monogram_no_space = dict(sorted(freq(Counter(text_no_space), count_letters(Counter(text_no_space))).items(), key=lambda item: item[1], reverse=True))
bigram_space = dict(sorted(freq(bigrams_counter(text_space, False), count_letters(bigrams_counter(text_space, False))).items(), key=lambda item: item[1], reverse=True))
bigram_no_space = dict(sorted(freq(bigrams_counter(text_no_space, False), count_letters(bigrams_counter(text_no_space, False))).items(), key=lambda item: item[1], reverse=True))
cross_bigram_space = dict(sorted(freq(bigrams_counter(text_space), count_letters(bigrams_counter(text_space))).items(), key=lambda item: item[1], reverse=True))
cross_bigram_no_space = dict(sorted(freq(bigrams_counter(text_no_space), count_letters(bigrams_counter(text_no_space))).items(), key=lambda item: item[1], reverse=True))

with open('../texts/monogram_space.txt', 'w') as file: 
    for key, val in monogram_space.items():
        file.write(f'{key} : {val}\n')
with open('../texts/monogram_no_space.txt', 'w') as file: 
    for key, val in monogram_no_space.items():
        file.write(f'{key} : {val}\n')

with open('../texts/bigram_space.txt', 'w') as file: 
    for key, val in bigram_space.items():
        file.write(f'{key} : {val}\n')
with open('../texts/bigram_no_space.txt', 'w') as file: 
    for key, val in bigram_no_space.items():
        file.write(f'{key} : {val}\n')

with open('../texts/cross_bigram_space.txt', 'w') as file: 
    for key, val in cross_bigram_space.items():
        file.write(f'{key} : {val}\n')
with open('../texts/cross_bigram_no_space.txt', 'w') as file: 
    for key, val in cross_bigram_no_space.items():
        file.write(f'{key} : {val}\n')

print_string = f"""
Монограми:

    Ентропія з пробілами: {entropy(monogram_space, True)}
    Надлишковість з пробілами: {calc_R(entropy(monogram_space, True))}

    Ентропія без пробілів: {entropy(monogram_no_space, True)}
    Надлишковість без пробілів: {calc_R(entropy(monogram_no_space, True))}

Біграми без перетину:

    Ентропія з пробілами: {entropy(bigram_space)}
    Надлишковість з пробілами: {calc_R(entropy(bigram_space))}

    Ентропія без пробілів: {entropy(bigram_no_space)}
    Надлишковість без пробілів: {calc_R(entropy(bigram_no_space))}

Біграми з перетином:

    Ентропія з пробілами: {entropy(cross_bigram_space)}
    Надлишковість з пробілами: {calc_R(entropy(cross_bigram_space))}

    Ентропія без пробілів: {entropy(cross_bigram_no_space)}
    Надлишковість без пробілів: {calc_R(entropy(cross_bigram_no_space))}
"""

print(print_string)
