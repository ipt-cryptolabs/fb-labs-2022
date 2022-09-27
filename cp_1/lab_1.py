import re

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

print(plainText + '\n')
print(noSpacesText)
