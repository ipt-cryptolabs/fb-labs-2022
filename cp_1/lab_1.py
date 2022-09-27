import re
from collections import Counter 
import math

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alphabetS = 'абвгдежзийклмнопрстуфхцчшщъыьэюя '

# відкрили файл, та  відформатували текст, отримали текст з пробілами, та текст - без
with open('cp_1/Война и мир.Том 2.Лев Толстой.txt', 'r', encoding='utf-8') as file:
    plainText = file.read().lower().replace('ъ', 'ь').replace('ё', 'е')
    plainText = re.compile(r'\s*[^а-яА-Я ]').sub('', plainText)
    reg = re.compile('[^а-яА-Я]')
    noSpacesText = reg.sub('', plainText)

with open('cp_1/plainText.txt', 'w', encoding='utf-8') as file:
    file.writelines(plainText)    
with open('cp_1/noSpacesText.txt', 'w', encoding='utf-8') as file:
    file.writelines(noSpacesText)


# print(plainText + '\n')
# print(noSpacesText)


def monogram(txt):
    #спочатку порахуємо частоту букв
    countedLetters = Counter(txt)
    for i in countedLetters.keys():
        # print(i)
        countedLetters[i] = countedLetters[i]/len(txt)
    #рахуємо ентропію за формулою з методички 
    # print(countedLetters)
    monog = 0
    for i in countedLetters.keys():
        # print(i)
        monog += (-countedLetters[i] * math.log2(countedLetters[i]))
        # print(f'ентропія для {i} : {(-countedLetters[i] * math.log2(countedLetters[i]))}'  )
    print(f'загальна ентропія для монограм: {monog}')
    return (monog)


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
    bigCount = 0
    for i in CrossBigram.keys():
        bigCount += (-CrossBigram[i] * math.log2(CrossBigram[i]))
        # print(f'ентропія для {i} : {(-CrossBigram[i] * math.log2(CrossBigram[i]))}')
    print(f'загальна ентропія для перехресної біграми: {bigCount/2}')
    print(f'надлишковість: {1 - (bigCount/2)/math.log2(32)}')

def NCbigrams(txt):
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
monogram(plainText)
print('Текст з пробілами')
bigrams(noSpacesText)
NCbigrams(noSpacesText)
monogram(noSpacesText)