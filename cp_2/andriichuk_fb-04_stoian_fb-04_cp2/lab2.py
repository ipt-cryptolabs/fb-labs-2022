from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def clean_text(text):
    new = ""
    text = text.lower().replace('ё', 'е')
    for i in text:
        if i in alphabet:
            new += i  
    return new

def index(text):
    sum_ = 0
    n = len(text)
    cnt = Counter(text)
    for value in cnt.values():
        sum_ += value * (value - 1)
    return sum_ / (n * (n - 1))

def kroneker(a, b):
    if a == b:
        return 1
    return 0

def D(text, key_len):
    n = len(text)
    D_sum = 0
    for i in range(n-key_len):
        D_sum += kroneker(text[i], text[i+key_len])
    return D_sum

def vegener_encrypt(text, key):
    new = ''
    key_iter = 0
    alphabet_len = len(alphabet)
    key_len = len(key)
    for x in text:
        x_ind = alphabet.index(x)
        k_ind = alphabet.index(key[key_iter])
        y_ind = (x_ind + k_ind) % alphabet_len
        key_iter = (key_iter + 1) % key_len
        new += alphabet[y_ind]
    return new

def vegener_decrypt(text, key):
    new = ''
    key_iter = 0
    alphabet_len = len(alphabet)
    key_len = len(key)
    for y in text:
        y_ind = alphabet.index(y)
        k_ind = alphabet.index(key[key_iter])
        x_ind = (y_ind - k_ind) % alphabet_len
        key_iter = (key_iter + 1) % key_len
        new += alphabet[x_ind]
    return new

def what_key(text, x):
    cnt = Counter(text)
    y = cnt.most_common(1)[0][0]
    y_ind = alphabet.index(y)
    x_ind = alphabet.index(x)
    key_ind = (y_ind - x_ind) % len(alphabet)
    return alphabet[key_ind]

keys = ['ты', 'иду', 'блиц', 'шторм', 'математика']
e = []

with open('task1.TXT', 'r', encoding='utf-8') as f:
    text = f.read()
    text = clean_text(text)

# 1
for key in keys:
    etext = vegener_encrypt(text, key)
    e.append(etext)
    print(f'key {key}\nencrypted text {etext}')


# 2
I = [index(text)]
for i in e:
    I.append(index(i))

lens = [0, 2, 3, 4, 5, 12]
for i in range(len(lens)):
    print(f'r = {lens[i]}: {I[i]}')

# 3
with open('v1_e.TXT', 'r', encoding='utf-8') as f:
    v1 = f.read()
    v1 = clean_text(v1)

for i in range(2, 33):
    print(f'r = {i}: D = {D(v1, i)}')

r = 12
vars = {'о':'', 'е':'', 'а':''}

for let in vars:
    for i in range(r):
        vars[let] += what_key(v1[i::r], let)
    print(vars[let])

key = 'вшекспирбуря'
v1_d = vegener_decrypt(v1, key)
with open('v1_d.TXT', 'w', encoding='utf-8') as f:
    f.write(v1_d)