from collections import Counter
import matplotlib.pyplot as plt

# # Фільтруємо текст
data_file = open('text_for_dect.txt', 'r', encoding='utf-8').read().lower().replace('ё', "е").replace("ъ", "ь")
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
filter_text = ''
for i in range(len(data_file)):
    if data_file[i] in alphabet:
        filter_text += data_file[i]
with open('filter_text.txt', 'w', encoding='utf-8') as file:
    file.write(filter_text)
variant_text = open('variant_text.txt', 'r', encoding='utf-8').read().replace('\n', '')
with open('variant_text.txt', 'w', encoding='utf-8') as file:
    file.write(variant_text)

keys_for_encr = ['чс', 'два', 'пара', 'слова', 'прочитатикнигупара']

# Функція для шифрування тексту по ключу
def encrypt(text, key):
    encrypt_text = ''
    value = 0
    for item in text:
        new_i = (alphabet.find(key[value]) + alphabet.find(item)) % len(alphabet)
        value = (value + 1) % len(key)
        encrypt_text += alphabet[new_i]

    return encrypt_text

# Шифруємо текст і записуємо
for key_value in keys_for_encr:
    encrypted_text = encrypt(filter_text, key_value)
    with open(f"{len(key_value)}_ecrypted.txt", 'w', encoding='utf-8') as file:
        file.write(encrypted_text)    

# Шукаємо індекс
def find_index(new_complite):
    count_index = Counter(new_complite)
    res = 0
    for i in count_index.values():
        res += (i * (i - 1))
    res /= (len(new_complite) * (len(new_complite) - 1))    
    return res

indexes = []
files = ['2_ecrypted.txt', '3_ecrypted.txt', '4_ecrypted.txt', '5_ecrypted.txt', '18_ecrypted.txt', 'filter_text.txt']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        res = find_index(text)
        indexes.append(res)
# print(indexes)

# # Дешифруємо
def textblocks(text, len_key):  #Поділ тексту на блоки
    blocks = []
    for cur_position in range(len_key):
        blocks.append(text[cur_position::len_key])
    return blocks

# print(textblocks(variant_text, 18))
def index_blocks(text): # індекси для блоків
    indexblock = dict()
    for key_len in range(2, 31):
        blocks = textblocks(variant_text, key_len)
        index = []
        for block in blocks:
            index.append(find_index(block))
        
        indexblock[key_len] = index.pop()
    return indexblock
# print(index_blocks(variant_text))

letters_freq = ['о', 'е', 'а', 'и', 'н', 'с', 'л', 'т', 'р', 'п', 'в', 'к', 'м', 'у', 'д', 'ч', 'ы', 'г', 'я', 'з', 'й', 'ь', 'х', 'б', 'ж', 'ю', 'щ', 'ш', 'ц', 'э']

def find_key():
    period = 15
    blocks = textblocks(variant_text, period)
    key = ""
    for block in blocks:
        letters_fq = Counter(block)
        key = key + max(letters_fq, key=letters_fq.get)
    letters = letters_freq
    res_key = ''
    for item in key:
        res_key += alphabet[(alphabet.find(item) - alphabet.find(letters[0])) % len(alphabet)]
    return res_key
print(find_key())

key = 'арудазовархимаг'

def decode(text, key):
    decrypt_text = ""
    for i in range(len(text)):
        decrypt_text = decrypt_text + alphabet[(alphabet.find(text[i]) - alphabet.find(key[i % len(key)])) % len(alphabet)]
    return decrypt_text

decrypt_text = decode(variant_text, key)
with open('decrypt_text.txt', 'w', encoding='utf-8') as file:
    file.write(decrypt_text)

# print(decode(variant_text, key))
