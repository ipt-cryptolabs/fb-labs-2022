from collections import Counter
import re
import pandas as pd

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def clear_txt(txt: str) -> str:
    patern = '[а-яА-я]{1,}'
    res = re.findall(pattern=patern, string=txt)
    res = ''.join(res)
    res = res.lower()
    res = res.replace('ё', 'е')
    return res

def I(txt: str) -> int:
    n = len(txt)
    coef = 1 / (n * (n - 1))
    summ = 0
    cnt = Counter(txt)
    for value in cnt.values():
        summ += value * (value - 1)
    return coef * summ

def MI(df: pd.DataFrame) -> int:
    summ = 0
    for i in df[0]:
        summ += i * i
    return summ

def guess_key(txt: str, symbol: str) -> str:
    global alphabet
    cnt = Counter(txt)
    len_ = len(txt)
    max_ = 0
    char = ''
    for i in cnt:
        cnt[i] /= len_
        if cnt[i] > max_:
            max_ = cnt[i]
            char = i
    char_ind = alphabet.index(char)
    symbol_ind = alphabet.index(symbol)
    new_ind = ((char_ind - symbol_ind) % 32 + 32) % 32
    return alphabet[new_ind]

def decrypt(txt: str, key: str) -> str:
    global alphabet
    res = ''
    for y in range(len(txt)):
        y_ind = alphabet.index(txt[y])
        x_ind = alphabet.index(key[y % len(key)])
        new_ind = ((y_ind - x_ind) % 32 + 32) % 32
        res += alphabet[new_ind]
    return res

def encrypt(txt: str, key: str) -> str:
    global alphabet
    res = ''
    for x in range(len(txt)):
        x_ind = alphabet.index(txt[x])
        k_ind = alphabet.index(key[x % len(key)])
        new_ind = (x_ind + k_ind) % 32
        res += alphabet[new_ind]
    return res