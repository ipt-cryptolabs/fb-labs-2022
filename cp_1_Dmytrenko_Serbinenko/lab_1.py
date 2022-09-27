import csv
import re
from collections import Counter 
import math
import pandas as pd

# відкрили файл, та  відформатували текст, отримали текст з пробілами, та текст - без
with open('cp_1_Dmytrenko_Serbinenko/Война и мир.Том 2.Лев Толстой.txt', 'r', encoding='utf-8') as file:
    plainText = file.read().lower().replace('ъ', 'ь').replace('ё', 'е')
    plainText = re.compile(r'\s*[^а-яА-Я ]').sub('', plainText)
    reg = re.compile('[^а-яА-Я]')
    noSpacesText = reg.sub('', plainText)

with open('cp_1_Dmytrenko_Serbinenko/plainText.txt', 'w', encoding='utf-8') as file:
    file.writelines(plainText)    
with open('cp_1_Dmytrenko_Serbinenko/noSpacesText.txt', 'w', encoding='utf-8') as file:
    file.writelines(noSpacesText)


# print(plainText + '\n')
# print(noSpacesText)


def monogram(txt, withSpace = False):
    #спочатку порахуємо частоту букв
    countedLetters = Counter(txt)
    df = pd.DataFrame(list(countedLetters.items()), columns=['Буква', 'Кількість повторів'])
    new_list = []
    for i in countedLetters.keys():
        # print(i)
        countedLetters[i] = countedLetters[i]/len(txt)
        new_list.append(countedLetters[i])
    df['Частота'] = new_list
    #рахуємо ентропію за формулою з методички 
    # print(countedLetters)
    monog = 0
    new_list = []
    for i in countedLetters.keys():
        # print(i)
        monog += (-countedLetters[i] * math.log2(countedLetters[i]))
        new_list.append((-countedLetters[i] * math.log2(countedLetters[i])))
        # print(f'ентропія для {i} : {(-countedLetters[i] * math.log2(countedLetters[i]))}'  )
    if withSpace == True:
        R = 1 - (monog/math.log2(32))
    else:
        R = 1 - (monog/math.log2(31))
    df['Ентропія для букви'] = new_list
    df.at[0, 'Ентропія'] = monog
    df.at[0, 'R'] = R
    print(f'загальна ентропія для монограм: {monog}')
    # df.to_csv(r'monogram.csv')
    if withSpace == True:
        df.to_excel('cp_1_Dmytrenko_Serbinenko/monogram_space.xlsx', index=False, sheet_name='Монограма з пробілами')
    else:
        df.to_excel('cp_1_Dmytrenko_Serbinenko/monogram.xlsx', index=False, sheet_name='Монограма без пробілів')
    return (monog)


def bigrams(txt, withSpace = False):
    CrossBigram = []
    for i in range(len(txt)):
        CrossBigram.append(txt[i:i+2]) # робимо список з 2х елементів 
    CrossBigram = Counter(CrossBigram) # завдяки класу Counter отримуємо тип даних dict де ключ - біграма, а значення - кількість повторів біграми
    # print(CrossBigram)
    for i in CrossBigram.keys(): # тут записуємо у наш словник для тих же ключів значення частоти
        # print(i)
        CrossBigram[i] = CrossBigram[i] / len(txt)
        # print(f'{i} : {CrossBigram[i]}')
    bigCount = 0
    for i in CrossBigram.keys():
        bigCount += (-CrossBigram[i] * math.log2(CrossBigram[i]))
        # print(f'ентропія для {i} : {(-CrossBigram[i] * math.log2(CrossBigram[i]))}')
    print(f'загальна ентропія для перехресної біграми: {bigCount/2}')
    print(f'надлишковість: {1 - (bigCount/2)/math.log2(32)}')

def NCbigrams(txt, withSpace = False):
    NCBigram = []
    txtLen = len(txt)
    if txtLen % 2 == 1:
        txtLen -= 1
    for i in range(txtLen):
        NCBigram.append(txt[i:i+2]) # робимо список з 2х елементів 
    NCBigram = Counter(NCBigram)
    for i in NCBigram.keys():
        NCBigram[i] = NCBigram[i] / txtLen    
    bigCount = 0
    for i in NCBigram.keys():
        bigCount += (-NCBigram[i] * math.log2(NCBigram[i]))
    print(f'загальна ентропія для не перехресної біграми: {bigCount/2}')
    print(f'надлишковість: {1 - (bigCount/2)/math.log2(32)}')

    

print('Текст з пробілами')
bigrams(plainText)
NCbigrams(plainText)
monogram(plainText, True)
print('Текст без пробілів')
bigrams(noSpacesText)
NCbigrams(noSpacesText)
monogram(noSpacesText)
