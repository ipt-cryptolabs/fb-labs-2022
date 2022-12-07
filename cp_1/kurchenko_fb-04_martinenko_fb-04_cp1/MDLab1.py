from collections import Counter
from math import log2
import pandas as pd
from xlsxwriter import Workbook


data_file = open('Двенадцать_стульев. Илья_Ильф_и_Евгений_Петров.txt', 'r', encoding='utf-8').read().lower().replace('ё', "е").replace("ъ", "ь")
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя '

filter_text = ''
for i in range(len(data_file)):
    if data_file[i] in alphabet:
        filter_text += data_file[i]

text_with_space = ''
for i in range(len(filter_text) - 1):
    if filter_text[i] == ' ' and filter_text[i+1] == ' ':
        continue
    else:
        text_with_space += filter_text[i]

text_without_space = text_with_space.replace(' ', '')

def count_letters_in_monogram(data):
    dict_count = {}
    
    for symvol in data:
        if symvol in dict_count:
            dict_count[symvol] += 1
        else:
            dict_count[symvol] = 1
    
    return dict_count

def frequency(data):
    count_all = 0
    for key, value in data.items():
        count_all += value

    for key in data:
        data[key] = data[key] / count_all 
    
    return data

def bigrams(data, is_crossed=True):
    dict_bigram = {}
    if is_crossed:
        for i in range(len(data)):
            if data[i:i+2] not in dict_bigram:
                dict_bigram[data[i:i+2]] = 1
            else:
                dict_bigram[data[i:i+2]] += 1
    else:
        for i in range(0, len(data), 2):
            if data[i:i+2] not in dict_bigram:
                dict_bigram[data[i:i+2]] = 1
            else:
                dict_bigram[data[i:i+2]] += 1

    return frequency(dict_bigram)

def entropy(data, n):
    entropy = 0
    for i in data:
        entropy += (-data[i] * log2(data[i]))
    
    return entropy / n

def calc_redurant(data, alphabet_len):
    return 1 - data / log2(alphabet_len)

mono_with_space = dict(sorted(frequency(count_letters_in_monogram(text_with_space)).items(), key=lambda item: item[1], reverse=True))
mono_without_space = dict(sorted(frequency(count_letters_in_monogram(text_without_space)).items(), key=lambda item: item[1], reverse=True))

bigram_with_space = dict(sorted(bigrams(text_with_space).items(), key=lambda item: item[1], reverse=True))
bigram_without_space = dict(sorted(bigrams(text_without_space).items(), key=lambda item: item[1], reverse=True))

cross_bigram_with_space = dict(sorted(bigrams(text_with_space, is_crossed=False).items(), key=lambda item: item[1], reverse=True))
cross_bigram_without_space = dict(sorted(bigrams(text_without_space, is_crossed=False).items(), key=lambda item: item[1], reverse=True))

table1 = pd.Series(data=mono_with_space)
table2 = pd.Series(data=mono_without_space)
table3 = pd.Series(data=bigram_with_space)
table4 = pd.Series(data=bigram_without_space)
table5 = pd.Series(data=cross_bigram_with_space)
table6 = pd.Series(data=cross_bigram_without_space)

with pd.ExcelWriter('Lab1.xlsx', engine='xlsxwriter') as writer:
    table1.to_excel(writer, sheet_name='Монограма з пробілами')
    table2.to_excel(writer, sheet_name='Монограма без пробілів')
    table3.to_excel(writer, sheet_name='Бі без перет з пробілами')
    table4.to_excel(writer, sheet_name='Бі без перет без пробілів')
    table5.to_excel(writer, sheet_name='Бі з перет з пробілами')
    table6.to_excel(writer, sheet_name='Бі з перет з порбілами')

entropy_mono_with_space = entropy(mono_with_space, 1)
reducant_mono_with_space = calc_redurant(entropy_mono_with_space, 32)
print(f'Монограми з пробілами\n Ентропія {entropy_mono_with_space}\nНадлишковість {reducant_mono_with_space}  ')

entropy_mono_without_space = entropy(mono_without_space, 1)
reducant_mono_without_space = calc_redurant(entropy_mono_without_space, 31)
print(f'Монограми без пробілів\n Ентропія {entropy_mono_without_space}\n Надлишковість {reducant_mono_without_space}  ')

entropy_bigram_with_space = entropy(bigram_with_space, 2)
reducant_bigram_with_space = calc_redurant(entropy_bigram_with_space, 32)
print(f'Біграми без перетину з пробілами\n Ентропія {entropy_bigram_with_space}\n Надлишковість {reducant_bigram_with_space}  ')

entropy_bigram_without_space = entropy(bigram_without_space, 2)
reducant_bigram_without_space = calc_redurant(entropy_bigram_without_space, 31)
print(f'Біграми без перетину без пробілів\n Ентропія {entropy_bigram_without_space}\n Надлишковість {reducant_bigram_without_space}  ')

entropy_cross_bigram_with_space = entropy(cross_bigram_with_space, 2)
reducant_cross_bigram_with_space = calc_redurant(entropy_cross_bigram_with_space, 32)
print(f'Біграми з перетином з пробілами\n Ентропія {entropy_cross_bigram_with_space}\n Надлишковість {reducant_cross_bigram_with_space}  ')

entropy_cross_bigram_without_space = entropy(cross_bigram_without_space, 2)
reducant_cross_bigram_without_space = calc_redurant(entropy_cross_bigram_without_space, 31)
print(f'Біграми з перетином без пробілів\n Ентропія {entropy_cross_bigram_without_space}\n Надлишковість {reducant_cross_bigram_without_space}  ')
