from math import log2
import re
import pandas as pd

def prepare_text_spaces(text):
    patern = '[а-яА-я]{1,}'
    res = re.findall(pattern=patern, string=text)
    res = ' '.join(res)
    res = res.lower()
    res = res.replace('ё', 'е').replace('ъ', 'ь')
    return res

def prepare_text_no_spaces(text):
    patern = '[а-яА-я]{1,}'
    res = re.findall(pattern=patern, string=text)
    res = ''.join(res)
    res = res.lower()
    res = res.replace('ё', 'е').replace('ъ', 'ь')
    return res

def monogram(txt):
    d = dict()
    txtlen = len(txt)
    for let in txt:
        if let not in d:
            d[let] = 1
        else:
            d[let] += 1
    count_ = sum(d.values())
    for let in d:
        d[let] /= count_
    return d
    

def bigram_cross(txt): #з перетинами
    txtlen = len(txt)
    d = dict()
    for i in range(txtlen): 
        bigram = txt[i:i+2]
        if bigram not in d: # d['as']
            d[bigram] = 1 
        else:
            d[bigram] += 1
    count_ = sum(d.values())
    for let in d:
        d[let] /= count_
    return d

def bigram_n_cross(txt): #без перетинів
    txtlen = len(txt)
    d = dict()
    for i in range(0, txtlen, 2):
        bigram = txt[i:i+2]
        if bigram not in d:
            d[bigram] = 1
        else:
            d[bigram] += 1
    count_ = sum(d.values())
    for let in d:
        d[let] /= count_
    return d

def entropy(dict_, n):
    entropy_ = 0
    for let in dict_:
        entropy_ += (-dict_[let] * log2(dict_[let]))
    return entropy_ / n

def redurant(entropy_, alph_len):
    return 1 - entropy_ / log2(alph_len)

with open('Nabokov_Lolita.txt', encoding='utf-8', mode='r') as file:
    text = file.read()

txt_space = prepare_text_spaces(text)
txt_no_space = prepare_text_no_spaces(text)

mono1 = monogram(txt_space) # 32
mono2 = monogram(txt_no_space) # 31
b1 = bigram_cross(txt_space)
b2 = bigram_n_cross(txt_space)
b3 = bigram_cross(txt_no_space)
b4 = bigram_n_cross(txt_no_space)


s1 = pd.Series(data=mono1)
s1 = s1.sort_values(ascending=False)
e1 = entropy(mono1, 1)
r1 = redurant(e1, 32)
print(f'Монограми з пробілами\nентропія {e1}\nнадлишковість {r1}')

s2 = pd.Series(data=mono2)
s2 = s2.sort_values(ascending=False)
e2 = entropy(mono2, 1)
r2 = redurant(e2, 31)
print(f'Монограми без пробілів\nентропія {e2}\nнадлишковість {r2}')

s3 = pd.Series(data=b1)
s3 = s3.sort_values(ascending=False)
e3 = entropy(b1, 2)
r3 = redurant(e3, 32)
print(f'Біграми з пробілами (з перетинами)\nентропія {e3}\nнадлишковість {r3}')

s4 = pd.Series(data=b2)
s4 = s4.sort_values(ascending=False)
e4 = entropy(b2, 2)
r4 = redurant(e4, 32)
print(f'Біграми з пробілами (без перетинів)\nентропія {e4}\nнадлишковість {r4}')

s5 = pd.Series(data=b3)
s5 = s5.sort_values(ascending=False)
e5 = entropy(b3, 2)
r5 = redurant(e5, 31)
print(f'Біграми без пробілів (з перетинами)\nентропія {e5}\nнадлишковість {r5}')

s6 = pd.Series(data=b4)
s6 = s6.sort_values(ascending=False)
e6 = entropy(b4, 2)
r6 = redurant(e6, 31)
print(f'Біграми без пробілів (без перетинів)\nентропія {e6}\nнадлишковість {r6}')


with pd.ExcelWriter('lab1.xlsx', engine='xlsxwriter') as writer:
    s1.to_excel(writer, sheet_name='Моногр з пробілами')
    s2.to_excel(writer, sheet_name='Моногр без пробілів')
    s3.to_excel(writer, sheet_name='Перехр бігр з пробілами')
    s4.to_excel(writer, sheet_name='Неперехр бігр з пробілами')
    s5.to_excel(writer, sheet_name='Перехр бігр без пробілів')
    s6.to_excel(writer, sheet_name='Неперехр бігр без пробілів')