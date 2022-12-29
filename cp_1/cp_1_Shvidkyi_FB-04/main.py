from collections import Counter
import math

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя '

file = open('Nabokov_Lolita.txt', 'r').read()
file = file.lower()
file = file.replace("ъ", "ь").replace('ё', "е").replace('\n', ' ')

text = ''
for i in file:
    if i in alphabet:
        text += i

text = ' '.join(text.split())
text_s = ''.join(text.split())

# write_text = open('my_text.txt', 'w')
# write_text.write(text)
# write_text.close()

# write_text = open('my_text_s.txt', 'w')
# write_text.write(text_s)
# write_text.close()

text_m = Counter(text)
text_m_s = Counter(text_s)

def to_bi(text, cross):
    bi_lst = []
    if cross == True:
        for i in range(len(text) - 1):
            bi_lst.append(text[i:i+2])
    elif cross == False:
        for i in range(0, len(text) - 1, 2):
            bi_lst.append(text[i:i+2])
    return Counter(bi_lst)

bigr = to_bi(text, False)
bigr_s = to_bi(text_s, False)
bigr_c = to_bi(text, True)
bigr_c_s = to_bi(text_s, True)

var_lst = [text_m, text_m_s, bigr, bigr_s, bigr_c, bigr_c_s]

def chast(counter):
    char_sum = 0
    for i in counter.values():
        char_sum += i
    for i in counter.keys():
        counter[i] = counter[i]/char_sum
    return counter

for i in var_lst:
    chast(i)

def writer(counter, name):
    with open(name, 'w') as file: 
        for key, val in counter.items():
            file.write(f'{key} : {val}\n')

writer(text_m, 'mono.txt')
writer(text_m_s, 'mono_s.txt')
writer(bigr, 'bigr.txt')
writer(bigr_s, 'bigr_s.txt')
writer(bigr_c, 'bigr_c.txt')
writer(bigr_c_s, 'bigr_c_s.txt')

def entropy(counter):
    for i in counter.keys():
        counter[i] = -(counter[i]*math.log2(counter[i]))
    return counter

for i in var_lst:
    entropy(i)

e_text_m = sum(text_m.values())
e_text_m_s = sum(text_m_s.values())
e_bigr = sum(bigr.values())/2
e_bigr_s = sum(bigr_s.values())/2
e_bigr_c = sum(bigr_c.values())/2
e_bigr_c_s = sum(bigr_c_s.values())/2

def nadl(entropy, isSpace=True):
    if isSpace == True:
        r = 1 - entropy / math.log2(31)
        return r
    else:
        r = 1 - entropy / math.log2(32)
        return r

r_text_m = nadl(e_text_m)
r_text_m_s = nadl(e_text_m_s)
r_bigr = nadl(e_bigr)
r_bigr_s = nadl(e_bigr_s)
r_bigr_c = nadl(e_bigr_c)
r_bigr_c_s = nadl(e_bigr_c_s)

print(f"""
Монограми:

    Ентропія з пробілами: {e_text_m}
    Ентропія без пробілів: {e_text_m_s}

    Надлишковість з пробілами: {r_text_m}
    Надлишковість без пробілів: {r_text_m_s}

Біграми без перетину:

    Ентропія з пробілами: {e_bigr}
    Ентропія без пробілів: {e_bigr_s}

    Надлишковість з пробілами: {r_bigr}
    Надлишковість без пробілів: {r_bigr_s}

Біграми з перетином:

    Ентропія з пробілами: {e_bigr_c}
    Ентропія без пробілів: {e_bigr_c_s}

    Надлишковість з пробілами: {r_bigr_c}
    Надлишковість без пробілів: {r_bigr_c_s}
""")