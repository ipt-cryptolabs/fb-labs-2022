from math import log2
import pandas as pd

def text_spaces(text):
    alphabet = "абвгдежзийклмнопрстуфхцчшщьэюя "
    new = ""
    text = text.lower().replace('ё', 'е').replace('ъ', 'ь')
    for i in text:
        if i in alphabet:
            new += i  
    return new.replace(' ', '_')

def text_no_spaces(text):
    alphabet = "абвгдежзийклмнопрстуфхцчшщьэюя"
    new = ""
    text = text.lower().replace('ё', 'е').replace('ъ', 'ь')
    for i in text:
        if i in alphabet:
            new += i  
    return new

def monogram(txt):
    d = dict()
    for i in txt:
        try:
            d[i] += 1
        except:
            d[i] = 1
    summ = sum(d.values())
    for i in d:
        d[i] /= summ
    return d
    

def bigram_with_cross(txt):
    d = dict()
    for i in range(len(txt)): 
        bigram = txt[i:i+2]
        try:
            d[bigram] += 1
        except:
            d[bigram] = 1        
    summ = sum(d.values())
    for i in d:
        d[i] /= summ
    return d

def bigram_with_no_cross(txt):
    d = dict()
    for i in range(0, len(txt), 2):
        bigram = txt[i:i+2]
        try:
            d[bigram] += 1
        except:
            d[bigram] = 1
    summ = sum(d.values())
    for i in d:
        d[i] /= summ
    return d

def entropy(dict_):
    entrop = 0
    for i in dict_:
        entrop += (-dict_[i] * log2(dict_[i])) / len(i)
    return entrop

def redurant(entrop, alph_len):
    return 1 - entrop / log2(alph_len)

with open('source.txt', encoding='utf-8', mode='r') as file:
    text = file.read()

txt_space = text_spaces(text)
txt_no_space = text_no_spaces(text)

m1 = monogram(txt_space)
m2 = monogram(txt_no_space)
b1 = bigram_with_cross(txt_space)
b2 = bigram_with_no_cross(txt_space)
b3 = bigram_with_cross(txt_no_space)
b4 = bigram_with_no_cross(txt_no_space)

e1 = entropy(m1)
e2 = entropy(m2)
e3 = entropy(b1)
e4 = entropy(b2)
e5 = entropy(b3)
e6 = entropy(b4)

r1 = redurant(e1, 32)
r2 = redurant(e2, 31)
r3 = redurant(e3, 32)
r4 = redurant(e4, 32)
r5 = redurant(e5, 31)
r6 = redurant(e6, 31)

s1 = pd.Series(m1).sort_values(ascending=False)
s2 = pd.Series(m2).sort_values(ascending=False)
s3 = pd.Series(b1).sort_values(ascending=False)
s4 = pd.Series(b2).sort_values(ascending=False)
s5 = pd.Series(b3).sort_values(ascending=False)
s6 = pd.Series(b4).sort_values(ascending=False)


print('Монограми з пробілами\nентропія {}\nнадлишковість {}'.format(e1, r1))
print('Монограми без пробілів\nентропія {}\nнадлишковість {}'.format(e2, r2))
print('Перехресні біграми з пробілами\nентропія {}\nнадлишковість {}'.format(e3, r3))
print('Неперехресні біграми з пробілами\nентропія {}\nнадлишковість {}'.format(e4, r4))
print('Перехресні біграми без пробілів\nентропія {}\nнадлишковість {}'.format(e5, r5))
print('Неперехресні біграми без пробілів\nентропія {}\nнадлишковість {}'.format(e6, r6))

with pd.ExcelWriter('lab1.xlsx', engine='xlsxwriter') as writer:
    s1.to_excel(writer, sheet_name='Мон з пробіл')
    s2.to_excel(writer, sheet_name='Мон без пробіл')
    s3.to_excel(writer, sheet_name='Перехр бігр з пробіл')
    s4.to_excel(writer, sheet_name='Неперехр бігр з пробіл')
    s5.to_excel(writer, sheet_name='Перехр бігр без пробіл')
    s6.to_excel(writer, sheet_name='Неперехр бігр без пробіл')