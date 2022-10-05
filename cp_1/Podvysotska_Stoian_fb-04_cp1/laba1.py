import re
from collections import Counter
import math


def removeSymbols(input, output):
    with open(input, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = text.replace('ё','е').replace('ъ','ь')
    text = re.sub('[^А-Яа-я]+|\n|\s', ' ', text)
    with open(output, 'w', encoding='utf-8') as file:
        file.write(text)
    # print(text)


def removeSpaces(input, output):
    with open(input, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = re.sub('\s', '', text)
    with open(output, 'w', encoding='utf-8') as file:
        file.write(text)
    # print(text)


removeSymbols('Deathly Hallows.txt', 'with_spaces.txt')
removeSpaces('with_spaces.txt', 'without_spaces.txt')


def coolMonograms(file):
    with open(file, 'r', encoding='utf-8') as pew:
        text = pew.read()
    counts = Counter(text)
    frequency = {item: counts.get(item) / len(text) for item in counts.keys()}
    frequency = dict(reversed(sorted(frequency.items(), key=lambda item: item[1])))
    entropy = sum(list(-freq * math.log2(freq) for freq in frequency.values()))
    if len(counts) == 32:
        redundancy = 1 - (entropy / math.log2(32))
    else:
        redundancy = 1 - (entropy / math.log2(31))
    print(counts, '\n')
    print('Frequency:', frequency, '\n')
    print('Entropy:', entropy, '\n')
    print('Redundancy:', redundancy, '\n\n')


def coolBigrams(file, intersections):
    with open(file, 'r', encoding='utf-8') as pew:
        text = pew.read()
    if intersections:
        bigrams = [text[i:i+2] for i in range (len(text))]
    else:
        bigrams = [text[i:i+2] for i in range (0, len(text), 2)]
    counts = Counter(bigrams)
    frequency = {item: counts.get(item) / len(text) for item in counts.keys()}
    frequency = dict(reversed(sorted(frequency.items(), key=lambda item: item[1])))
    entropy = 0.5 * sum(list(-freq * math.log2(freq) for freq in frequency.values()))
    if len(counts) == 32:
        redundancy = 1 - (entropy / math.log2(32))
    else:
        redundancy = 1 - (entropy / math.log2(31))
    print(counts, '\n')
    print('Frequency:', frequency, '\n')
    print('Entropy:', entropy, '\n')
    print('Redundancy:', redundancy, '\n\n')


print('MONOGRAMS WITH SPACES', '\n')
coolMonograms('with_spaces.txt')

print('MONOGRAMS WITHOUT SPACES', '\n')
coolMonograms('without_spaces.txt')

print('BIGRAMS WITH SPACES', '\n')
coolBigrams('with_spaces.txt', False)

print('BIGRAMS WITHOUT SPACES', '\n\n')
coolBigrams('without_spaces.txt', False)

print('BIGRAMS WITH SPACES & WITH INTERSECTIONS', '\n')
coolBigrams('with_spaces.txt', True)

print('BIGRAMS WITHOUT SPACES & WITH INTERSECTIONS', '\n')
coolBigrams('without_spaces.txt', True)