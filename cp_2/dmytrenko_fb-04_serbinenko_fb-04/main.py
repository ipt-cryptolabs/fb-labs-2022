import random

# file = open('se.txt').read().lower().replace('\n', '').replace(' ', '').replace('ё', 'е').replace('ъ', 'ь')

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'

# txt = ''
# for i in file:
#     if i in alphabet:
#         txt += i

# print(txt)

# with open('pt.txt', 'w') as file:
#     file.write(txt)

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

key_gen()
print(keys)