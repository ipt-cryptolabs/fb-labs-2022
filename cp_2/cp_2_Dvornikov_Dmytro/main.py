import re
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from collections import Counter

fig, ax = plt.subplots()
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

mod = len(alphabet)
rules = r'[^а-яА-Я ]'

keys = ['за', 'усы', 'небо', 'каска', 'астрономический']

most_frequenct_letters = 'оеаинт'


def text_filter(text: str) -> str:
    return re.sub(rules, "", text).replace(" ", "").replace("ё", "е").lower()


def open_file(file) -> str:
    with open(file, "r") as text:
        return text_filter(text.read())


open_text = open_file("open_text.txt")
cipher_text = open_file("var8_dvornikov.txt")


def vigenere(ciphertext: str, key: str, mode: str) -> str:
    outputtext = ""
    key_index = 0
    if mode == "decrypt":
        for letter in ciphertext:
            outputtext += alphabet[(alphabet.index(letter) + mod - alphabet.index(key[key_index % len(key)])) % mod]
            key_index += 1
    elif mode == "encrypt":
        for letter in ciphertext:
            outputtext += alphabet[(alphabet.index(letter) + alphabet.index(key[key_index % len(key)])) % mod]
            key_index += 1
    else:
        return "input error"
    return outputtext


def counter(text: str) -> dict:
    return dict(sorted(Counter(text).items(), key=lambda x: x[1], reverse=True))


def frequency(text: str) -> list:
    chars = counter(text)
    char_sum = 0
    for char in chars.values():
        char_sum += char
    return sorted({char: round((count / char_sum), 5) for char, count in chars.items()}.items(), key=lambda x: x[1],
                  reverse=True)


def find_index(text: str) -> float:
    compliance = 0
    chars = counter(text)
    for char in chars:
        compliance += chars[char] * (chars[char] - 1)
    return compliance / (len(text) * (len(text) - 1))


def get_block_compliance(text: str) -> dict:
    compliance_block = {}
    for key_length in range(2, 31):
        result_blocks = []
        for step in range(key_length):
            result_blocks.append(find_index(text[step::key_length]))
        compliance_block[key_length] = sum(result_blocks) / key_length
    return compliance_block


def find_key(text: str, keylenght: int, letter: str) -> str:
    blocks = [text[j::keylenght] for j in range(keylenght)]
    key = ''
    for b in blocks:
        most_common_letter = Counter(b).most_common(1)[0]
        key += alphabet[(alphabet.index(most_common_letter[0]) - alphabet.index(letter)) % 32]
    return key


for letter in most_frequenct_letters:
    key = find_key(cipher_text, 20, letter)
    print(key)

res_key = 'улановсеребряныепули'

name = get_block_compliance(cipher_text)
print(name)
print(find_index(open_text))
print(find_index(cipher_text))

plt.bar(name.keys(), name.values())
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.title("Complience index for keys")

index_for_diff_length = []

for i in keys:
    with open(f"Key with length {len(i)}.txt", 'w', encoding="utf-8") as file:
        some_text = vigenere(open_text, i, "encrypt")
        index_for_diff_length.append(find_index(some_text))
        file.write(some_text)
        file.close()
plt.bar(keys, index_for_diff_length)
plt.title("Complience index")

print(vigenere(cipher_text, res_key, "decrypt"))

with open(f"decoded_text.txt", 'w', encoding="utf-8") as file:
    file.write(vigenere(cipher_text, res_key, "decrypt"))
