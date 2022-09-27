import re
from collections import Counter

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabetS = 'абвгдежзийклмнопрстуфхцчшщъыьэюя '

# відкрили файл, та  відформатували текст, отримали текст з пробілами, та текст - без
with open('cp_1/ex.txt', 'r', encoding='utf-8') as file:
    plainText = file.read().lower().replace('ъ', 'ь').replace('ё', 'е')
    plainText = re.compile(r'\s*[^а-яА-Я ]').sub('', plainText)
    reg = re.compile('[^а-яА-Я]')
    noSpacesText = reg.sub('', plainText)

with open('cp_1/plainText.txt', 'w', encoding='utf-8') as file:
    file.writelines(plainText)    
with open('cp_1/noSpacesText.txt', 'w', encoding='utf-8') as file:
    file.writelines(noSpacesText)

def bigrams(txt):
    CrossBigram = []
    for i in range(len(txt)):
        CrossBigram.append(txt[i:i+2]) # робимо список з 2х елементів 
    CrossBigram = Counter(CrossBigram) # завдяки класу Counter отримуємо тип даних dict де ключ - біграма, а значення - кількість повторів біграми
    # print(CrossBigram)
    for i in CrossBigram.keys(): # тут записуємо у наш словник для тих же ключів значення частоти
        # print(i)
        CrossBigram[i] = CrossBigram[i] / len(txt)
        # print(f'{i} : {CrossBigram[i]}')
bigrams(plainText)