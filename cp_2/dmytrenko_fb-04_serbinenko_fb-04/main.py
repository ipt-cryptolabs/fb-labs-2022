import random
from collections import Counter

# file = open('se.txt').read().lower().replace('\n', '').replace(' ', '').replace('ё', 'е').replace('ъ', 'ь')

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
# txt = ''
# for i in file:
#     if i in alphabet:
#         txt += i

# print(txt)

# with open('pt.txt', 'w') as file:
#     file.write(txt)

text = open('pt.txt', 'r', encoding='utf-8').read()
var_text = open('var_text.txt', 'r', encoding='utf-8').read()

### завдання 1 ###
keys = []

def key_gen():
    for i in range(2, 6):
        j = 0
        key= ''
        while j < i:
            key += ''.join(random.choice(alphabet))
            j += 1
        keys.append(key)

    for i in range(10, 21):
        key= ''
        j = 0
        while j < i:
            key += ''.join(random.choice(alphabet))
            j += 1
        keys.append(key)

def encrypt(txt: str, keys: list):
    with open('encrypted_text.txt', 'w+', encoding='utf-8') as file:
        index = index_counter(txt)
        file.write(f'Our plain text\nindex: {index}\ntext:\n{txt}\n\n')
        
        for key in keys:
            encrypted = []
            for i in range(len(txt)):
                letter = alphabet[(alphabet.index(txt[i]) + alphabet.index(key[i % len(key)]))%len(alphabet)]
                encrypted.append(letter)
            enc_txt = ''.join(encrypted)
            index = index_counter(encrypted)
            file.write(f'key: {key}\nindex: {index}\ntext:\n{enc_txt}\n\n')

def index_counter(txt: str):
    plait_text = Counter(txt)
    index = 0
    for i in plait_text:
        index += plait_text[i]*(plait_text[i] - 1)
    text_sum = sum(plait_text.values())
    index /= text_sum*(text_sum - 1)
    return index

# key_gen()
# encrypt(text, keys)

### завдання 2 ###

def search():
    count = {}
    for i in range(1, 31):
        blocks = []
        for j in range(i):
            blocks.append(var_text[j::i])
        index = 0
        for block in blocks:
            index += index_counter(block)
        index /= i
        count[i] = index
    return count
    

def key_founder(len_key):
    blocks = []
    for i in range(len_key):
        blocks.append(var_text[i::len_key])

    top = 'аео'
    for letter in top:
        key = ''
        for block in blocks:
            block_lst = []
            for i in range(len(block)):
                block_lst.append(block[i])
            blocksCalc = Counter(block_lst)
            maxCalc = max(blocksCalc, key=blocksCalc.get)
            key_letter = alphabet[(alphabet.index(maxCalc) - alphabet.index(letter))%len(alphabet)]
            key += key_letter
        print(key)
        
    


def decrypt(key, text):
    answer = []
    for i in range(len(text)):
        key_letter = alphabet[(alphabet.index(text[i]) - alphabet.index(key[i % len(key)]))%len(alphabet)]
        answer.append(key_letter)
    answer = ''.join(answer)
    return answer
    

index_dict = search()
print(index_dict)
# key_len = max(index_dict, key=index_dict.get)
key_len = 14
key_founder(key_len)
'''
фуярцтыцчтьхьюэьящуйхцотущью
поълснцстнчрчщшчъфодрсйнофчщ
жесвиднийдозорпослеызиаделор # последнийдозор
'''
key = 'последнийдозор'
answer = decrypt(key, var_text)
with open('answer.txt', 'w', encoding='utf-8') as file:
    file.write(answer)