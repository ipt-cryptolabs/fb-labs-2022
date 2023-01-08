from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def right_text(text):
    res = ''
    for i in text:
        if i in alphabet:
            res += i
    return res

def Index(text):
    _sum = 0
    _len = len(text)
    c = Counter(text)
    for count in c.values():
        _sum += count * (count - 1)
    return _sum / (_len * (_len - 1))

def gimmy_key(text, x):
    cnt = Counter(text)
    y = cnt.most_common(1)[0][0]
    y_ind = alphabet.index(y)
    x_ind = alphabet.index(x)
    key_ind = (y_ind - x_ind) % len(alphabet)
    return alphabet[key_ind]
    # char = Counter(txt).most_common(1)[0][0]
    # char_ind = alphabet.index(char)
    # symbol_ind = alphabet.index(ch)
    # new_ind = (char_ind - symbol_ind) % 32
    # return alphabet[new_ind]

def encrypt(text, key):
    res = ''
    for x in range(len(text)):
        _x = alphabet.index(text[x])
        _key = alphabet.index(key[x % len(key)])
        new_ind = (_x + _key) % 32
        res += alphabet[new_ind]
    return res

def decrypt(txt: str, key: str) -> str:
    res = ''
    for y in range(len(txt)):
        _y = alphabet.index(txt[y])
        _x = alphabet.index(key[y % len(key)])
        new_ind = (_y - _x) % 32
        res += alphabet[new_ind]
    return res