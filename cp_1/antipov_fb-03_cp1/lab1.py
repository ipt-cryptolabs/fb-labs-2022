import math

alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя "


def text_with_spaces(file_input, file_output):
    with open(file_input, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = text.replace('ё', 'е').replace('ъ', 'ь').replace('\n', ' ')
    result = ''
    for i in text:
        if i in alphabet:
            result += i
    result = result.replace('  ', ' ')
    with open(file_output, 'w', encoding='utf-8') as file:
        file.write(result)


text_with_spaces('harry.txt', 'harry_with_spaces.txt')


def text_without_spaces(file_input, file_output):
    with open(file_input, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.replace(' ', '')
    with open(file_output, 'w', encoding='utf-8') as file:
        file.write(text)


text_without_spaces('harry_with_spaces.txt', 'harry_without_spaces.txt')


def freqency(text):
    d = {}
    for i in text:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for letter in d:
        d[letter] = d[letter] / len(text)
    return d


file_with_spaces = open('harry_with_spaces.txt', encoding='utf-8')
freq_with_spaces = file_with_spaces.read()
print("Частота літер у тексті з пробілами:\n ", freqency(freq_with_spaces))

file_without_spaces = open('harry_without_spaces.txt', encoding='utf-8')
freq_without_spaces = file_without_spaces.read()
print("Частота літер у тексті без пробілів:\n ", freqency(freq_without_spaces))


def entropy(d, n):
    ans = 0
    for i in d.values():
        ans += - i * math.log(i, 2)
    ans *= 1 / n
    return ans


entropy_with_spaces = entropy(freqency(freq_with_spaces), 1)
print("H1 з пробілами: ", entropy_with_spaces)

redurancy_with_spaces = 1 - entropy_with_spaces / math.log2(len(alphabet))
print("Надлишковість з пробілами: ", redurancy_with_spaces)

entropy_without_spaces = entropy(freqency(freq_without_spaces), 1)
print("H1 без пробілів: ", entropy_without_spaces)

redurancy_without_spaces = 1 - entropy_without_spaces / math.log2(len(alphabet))
print("Надлишковість без пробілів: ", redurancy_without_spaces)










