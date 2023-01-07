import re
from math import log2
from collections import Counter

rules = r"[^А-Яа-я ]"


def text_filter(text: str, space: str) -> str:
    return re.sub(rules, "", text).replace("  ", " ").replace(" ", "*").lower() if space == "yes" else re.sub(rules, "",
                                                                                                              text).replace(
        "  ", " ").replace(" ", "").lower()


def open_file(file, space: str) -> str:
    with open(file, "r") as text:
        return text_filter(text.read(), "yes") if space == "yes" else text_filter(text.read(), "no")


def counter(text: str) -> dict:
    return dict(sorted(Counter(text).items(), key=lambda x: x[1], reverse=True))


def frequency(text: str) -> list:
    chars = counter(text)
    char_sum = 0
    for char in chars.values():
        char_sum += char
    return sorted({char: round((count / char_sum), 5) for char, count in chars.items()}.items(), key=lambda x: x[1],
                  reverse=True)


def bigram_frequency(text: str, step: str) -> list or str:
    bigram_sum = 0
    if step.lower() == "slide":
        birgams = [text[i:i + 2] for i in range(0, len(text) - 1, 1)]
    elif step.lower() == "block":
        birgams = [text[i:i + 2] for i in range(0, len(text) - 1, 2)]
    else:
        return "input error"
    bigrams_count = Counter(birgams)
    for bigram in bigrams_count.values():
        bigram_sum += bigram
    bigrams_frequency = sorted({char: round((count / bigram_sum), 5) for char, count in bigrams_count.items()}.items(),
                               key=lambda x: x[1],
                               reverse=True)
    return bigrams_frequency


def find_h(prepared_text: list, n: int) -> float:
    h = 0
    for char in prepared_text:
        if char[1] <= 0:
            continue
        h += -char[1] * log2(char[1])
    h = h * 1 / n

    return h


def find_R(h: float, alphabet: int) -> float:
    return 1 - h / log2(alphabet)


alphabet_space = 34
alphabet_no_space = 33

text_space = open_file("open_text.txt", "yes")
text_no_space = open_file("open_text.txt", "no")

text_space_frequency = frequency(text_space)
# print(text_space_frequency)

text_no_space_frequency = frequency(text_no_space)
# print(text_no_space_frequency)

slide_bigrams_space_frequency = bigram_frequency(text_space, "slide")
# print(slide_bigrams_space_frequency)

block_bigrams_space_frequency = bigram_frequency(text_space, "block")
# print(block_bigrams_space_frequency)

slide_bigrams_no_space_frequency = bigram_frequency(text_no_space, "slide")
# print(slide_bigrams_no_space_frequency)

block_bigrams_no_space_frequency = bigram_frequency(text_no_space, "block")
# print(block_bigrams_no_space_frequency)

h1_text_space = find_h(text_space_frequency, 1)
print(h1_text_space, "- Ентропія для тексту з пробілом", "\n")

h1_text_no_space = find_h(text_no_space_frequency, 1)
print(h1_text_no_space, "- Ентропія для тексту без пробілів", "\n")

r_text_space = find_R(h1_text_space, alphabet_space)
print(r_text_space, "- Надлишковість для тексту з пробілом", "\n")

r_text_no_space = find_R(h1_text_no_space, alphabet_no_space)
print(r_text_no_space, "- Надлишковість для тексту без пробілів", "\n")

h2_slide_space = find_h(slide_bigrams_space_frequency, 2)
print(h2_slide_space, "- Ентропія для перехресних біграм з пробілом", "\n")

h2_block_space = find_h(block_bigrams_space_frequency, 2)
print(h2_block_space, "- Ентропія для не перехресних біграм без пробілів", "\n")

h2_slide_no_space = find_h(slide_bigrams_no_space_frequency, 2)
print(h2_slide_no_space, "- Ентропія для перехресних біграм з пробілом", "\n")

h2_block_no_space = find_h(block_bigrams_no_space_frequency, 2)
print(h2_block_no_space, "- Ентропія для не перехресних біграм без пробілів", "\n")

r_slide_space = find_R(h2_slide_space, alphabet_space)
print(r_slide_space, "- Надлишковість для перехресних біграм з пробілом", "\n")

r_block_space = find_R(h2_block_space, alphabet_space)
print(r_block_space, "- Надлишковість для не перехресних біграм з пробілом", "\n")

r_slide_no_space = find_R(h2_slide_no_space, alphabet_no_space)
print(r_slide_no_space, "- Надлишковість для перехресних біграм без пробілів", "\n")

r_block_no_space = find_R(h2_block_no_space, alphabet_no_space)
print(r_block_no_space, "- Надлишковість для не перехресних біграм без пробілів", "\n")

with open("text_space_frequency.txt", 'w', encoding='utf-8') as f:
    for key, value in text_space_frequency:
        f.write('%s : %s\n' % (key, value))
with open("text_no_space_frequency.txt", 'w', encoding='utf-8') as f:
    for key, value in text_no_space_frequency:
        f.write('%s : %s\n' % (key, value))
with open("block_bigrams_space_frequency.txt", 'w', encoding='utf-8') as f:
    for key, value in block_bigrams_space_frequency:
        f.write('%s : %s\n' % (key, value))
with open("slide_bigrams_space_frequency.txt", 'w', encoding='utf-8') as f:
    for key, value in slide_bigrams_space_frequency:
        f.write('%s : %s\n' % (key, value))
with open("block_bigrams_no_space_frequency.txt", 'w', encoding='utf-8') as f:
    for key, value in block_bigrams_no_space_frequency:
        f.write('%s : %s\n' % (key, value))
with open("slide_bigrams_no_space_frequency.txt", 'w', encoding='utf-8') as f:
    for key, value in slide_bigrams_no_space_frequency:
        f.write('%s : %s\n' % (key, value))
