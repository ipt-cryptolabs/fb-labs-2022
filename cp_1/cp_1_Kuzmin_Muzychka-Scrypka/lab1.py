import math
import pandas as pd

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
with open('C:/Users/Gleb/Desktop/file.txt', encoding='utf-8') as file:
    oldfile = file.read().lower()
oldfile = oldfile.replace('ё', 'е').replace('ъ', 'ь')
space = 0
TextSpace = ''
for elem in oldfile:
    if elem not in alphabet and elem != ' ':
        oldfile = oldfile.replace(elem, '')
for elem in oldfile:
    if elem == ' ':
        space += 1
    else:
        space = 0
    if space < 2:
        TextSpace = TextSpace + elem
TextNoSpace = TextSpace.replace(' ', '')

MonoSpaceLetter = [' ']
MonoSpaceCount = [0]
BigramSpaceCrossedLetter = []
BigramSpaceCrossedCount = []

for letter in alphabet:
    MonoSpaceLetter.append(letter)
    MonoSpaceCount.append(0)
for i in range(len(MonoSpaceLetter)):
    MonoSpaceCount[i] = TextSpace.count(MonoSpaceLetter[i])
    for x in range(len(MonoSpaceLetter)):
        BigramSpaceCrossedLetter.append(MonoSpaceLetter[i] + MonoSpaceLetter[x])
        BigramSpaceCrossedCount.append(0)

MonoNoSpaceLetter = MonoSpaceLetter[1:]
MonoNoSpaceCount = MonoSpaceCount[1:]

BigramNoSpaceCrossedLetter = []
BigramNoSpaceCrossedCount = []
for i in range(len(BigramSpaceCrossedLetter)):
    BigramSpaceCrossedCount[i] = TextSpace.count(BigramSpaceCrossedLetter[i])
    if ' ' != BigramSpaceCrossedLetter[i][0] and ' ' != BigramSpaceCrossedLetter[i][1]:
        BigramNoSpaceCrossedLetter.append(BigramSpaceCrossedLetter[i])
        BigramNoSpaceCrossedCount.append([0])
for i in range(len(BigramNoSpaceCrossedLetter)):
    BigramNoSpaceCrossedCount[i] = TextNoSpace.count(BigramNoSpaceCrossedLetter[i])

BigramSpaceNoCrossedLetter = BigramSpaceCrossedLetter
BigramSpaceNoCrossedCount = [0] * len(BigramSpaceNoCrossedLetter)
first = 0
second = 2
while second <= len(TextSpace):
    BigramSpaceNoCrossedCount[BigramSpaceNoCrossedLetter.index(TextSpace[first:second])] += 1
    first += 2
    second += 2

BigramNoSpaceNoCrossedLetter = BigramNoSpaceCrossedLetter
BigramNoSpaceNoCrossedCount = [0] * len(BigramNoSpaceNoCrossedLetter)
first = 0
second = 2
while second <= len(TextNoSpace):
    BigramNoSpaceNoCrossedCount[BigramNoSpaceNoCrossedLetter.index(TextNoSpace[first:second])] += 1
    first += 2
    second += 2

#Частота
MonoSpaceFreq = []
for i in range(len(MonoSpaceCount)):
    MonoSpaceFreq.append(MonoSpaceCount[i] / len(TextSpace))

MonoNoSpaceFreq = []
for i in range(len(MonoNoSpaceCount)):
    MonoNoSpaceFreq.append(MonoNoSpaceCount[i] / len(TextNoSpace))

BigramSpaceCrossedFreq = []
for i in range(len(BigramSpaceCrossedCount)):
    BigramSpaceCrossedFreq.append(BigramSpaceCrossedCount[i] / (len(TextSpace) - 1))

BigramNoSpaceCrossedFreq = []
for i in range(len(BigramNoSpaceCrossedCount)):
    BigramNoSpaceCrossedFreq.append(BigramNoSpaceCrossedCount[i] / (len(TextNoSpace) - 1))

BigramSpaceNoCrossedFreq = []
counter = 0
for elem in BigramSpaceNoCrossedCount:
    counter += elem
for i in range(len(BigramSpaceNoCrossedCount)):
    BigramSpaceNoCrossedFreq.append(BigramSpaceNoCrossedCount[i] / counter)

BigramNoSpaceNoCrossedFreq = []
counter = 0
for elem in BigramNoSpaceNoCrossedCount:
    counter += elem
for i in range(len(BigramNoSpaceNoCrossedCount)):
    BigramNoSpaceNoCrossedFreq.append(BigramNoSpaceNoCrossedCount[i] / counter)

#Ентропія
MonoSpaceLocalEntropy = []
MonoSpaceEntropy = 0
for i in range(len(MonoSpaceFreq)):
    if MonoSpaceFreq[i] == 0:
        MonoSpaceLocalEntropy.append(0)
    else:
        MonoSpaceLocalEntropy.append( - (MonoSpaceFreq[i] * math.log(MonoSpaceFreq[i], 2)))
        MonoSpaceEntropy -= MonoSpaceFreq[i] * math.log(MonoSpaceFreq[i], 2)

MonoNoSpaceLocalEntropy = []
MonoNoSpaceEntropy = 0
for i in range(len(MonoNoSpaceFreq)):
    if MonoNoSpaceFreq[i] == 0:
        MonoNoSpaceLocalEntropy.append(0)
    else:
        MonoNoSpaceLocalEntropy.append( - (MonoNoSpaceFreq[i] * math.log(MonoNoSpaceFreq[i], 2)))
        MonoNoSpaceEntropy -= MonoNoSpaceFreq[i] * math.log(MonoNoSpaceFreq[i], 2)

BigramSpaceCrossedLocalEntropy = []
BigramSpaceCrossedEntropy = 0
for i in range(len(BigramSpaceCrossedFreq)):
    if BigramSpaceCrossedFreq[i] == 0:
        BigramSpaceCrossedLocalEntropy.append(0)
    else:
        BigramSpaceCrossedLocalEntropy.append( - (BigramSpaceCrossedFreq[i] * math.log(BigramSpaceCrossedFreq[i], 2)))
        BigramSpaceCrossedEntropy -= ((BigramSpaceCrossedFreq[i] * math.log(BigramSpaceCrossedFreq[i], 2)) / 2)

BigramSpaceNoCrossedLocalEntropy = []
BigramSpaceNoCrossedEntropy = 0
for i in range(len(BigramSpaceNoCrossedFreq)):
    if BigramSpaceNoCrossedFreq[i] == 0:
        BigramSpaceNoCrossedLocalEntropy.append(0)
    else:
        BigramSpaceNoCrossedLocalEntropy.append( - (BigramSpaceNoCrossedFreq[i] * math.log(BigramSpaceNoCrossedFreq[i], 2)))
        BigramSpaceNoCrossedEntropy -= ((BigramSpaceNoCrossedFreq[i] * math.log(BigramSpaceNoCrossedFreq[i], 2)) / 2)

BigramNoSpaceCrossedLocalEntropy = []
BigramNoSpaceCrossedEntropy = 0
for i in range(len(BigramNoSpaceCrossedFreq)):
    if BigramNoSpaceCrossedFreq[i] == 0:
        BigramNoSpaceCrossedLocalEntropy.append(0)
    else:
        BigramNoSpaceCrossedLocalEntropy.append( - (BigramNoSpaceCrossedFreq[i] * math.log(BigramNoSpaceCrossedFreq[i], 2)))
        BigramNoSpaceCrossedEntropy -= ((BigramNoSpaceCrossedFreq[i] * math.log(BigramNoSpaceCrossedFreq[i], 2)) / 2)

BigramNoSpaceNoCrossedLocalEntropy = []
BigramNoSpaceNoCrossedEntropy = 0
for i in range(len(BigramNoSpaceNoCrossedFreq)):
    if BigramNoSpaceNoCrossedFreq[i] == 0:
        BigramNoSpaceNoCrossedLocalEntropy.append(0)
    else:
        BigramNoSpaceNoCrossedLocalEntropy.append( - (BigramNoSpaceNoCrossedFreq[i] * math.log(BigramNoSpaceNoCrossedFreq[i], 2)))
        BigramNoSpaceNoCrossedEntropy -= ((BigramNoSpaceNoCrossedFreq[i] * math.log(BigramNoSpaceNoCrossedFreq[i], 2)) / 2)

#Надлишковість
MonoSpaceRedundancy = 1 - (MonoSpaceEntropy / math.log(32, 2))

MonoNoSpaceRedundancy = 1 - (MonoNoSpaceEntropy / math.log(31, 2))

BigramSpaceCrossedRedundancy = 1 - (BigramSpaceCrossedEntropy / math.log(32, 2))

BigramSpaceNoCrossedRedundancy = 1 - (BigramSpaceNoCrossedEntropy / math.log(32, 2))

BigramNoSpaceCrossedRedundancy = 1 - (BigramNoSpaceCrossedEntropy / math.log(31, 2))

BigramNoSpaceNoCrossedRedundancy = 1 - (BigramNoSpaceNoCrossedEntropy / math.log(31, 2))

#Прінти
print('--Текст з пробілами:')
print('Загальна ентропія для монограм:', MonoSpaceEntropy)
print('Надлишковість:', MonoSpaceRedundancy)
print('Загальна ентропія для перехресних біграм:', BigramSpaceCrossedEntropy)
print('Надлишковість:', BigramSpaceCrossedRedundancy)
print('Загальна ентропія для неперехресних біграм:', BigramSpaceNoCrossedEntropy)
print('Надлишковість:', BigramSpaceNoCrossedRedundancy)
print('--Текст без пробілів:')
print('Загальна ентропія для монограм:', MonoNoSpaceEntropy)
print('Надлишковість:', MonoNoSpaceRedundancy)
print('Загальна ентропія для перехресних біграм:', BigramNoSpaceCrossedEntropy)
print('Надлишковість:', BigramNoSpaceCrossedRedundancy)
print('Загальна ентропія для неперехресних біграм:', BigramNoSpaceNoCrossedEntropy)
print('Надлишковість:', BigramNoSpaceNoCrossedRedundancy)

#Парсінг
writer = pd.ExcelWriter('result.xlsx', engine = 'xlsxwriter')
column = pd.DataFrame(MonoSpaceLetter)
column.insert(1, "Кількість", MonoSpaceCount)
column.insert(2, "Частота", MonoSpaceFreq)
column.insert(3, "Ентропія", MonoSpaceLocalEntropy)
column.to_excel(writer, 'Монограми з пробілами')
writer.save()

writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode = 'a')
column = pd.DataFrame(MonoNoSpaceLetter)
column.insert(1, "Кількість", MonoNoSpaceCount)
column.insert(2, "Частота", MonoNoSpaceFreq)
column.insert(3, "Ентропія", MonoNoSpaceLocalEntropy)
column.to_excel(writer, 'Монограми без пробілів')
writer.save()

writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode = 'a')
column = pd.DataFrame(BigramSpaceCrossedLetter)
column.insert(1, "Кількість", BigramSpaceCrossedCount)
column.insert(2, "Частота", BigramSpaceCrossedFreq)
column.insert(3, "Ентропія", BigramSpaceCrossedLocalEntropy)
column.to_excel(writer, 'Біграми з пробілами та з перетинами')
writer.save()

writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode = 'a')
column = pd.DataFrame(BigramSpaceNoCrossedLetter)
column.insert(1, "Кількість", BigramSpaceNoCrossedCount)
column.insert(2, "Частота", BigramSpaceNoCrossedFreq)
column.insert(3, "Ентропія", BigramSpaceNoCrossedLocalEntropy)
column.to_excel(writer, 'Біграми з пробілами та без перетинів')
writer.save()

writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode = 'a')
column = pd.DataFrame(BigramNoSpaceCrossedLetter)
column.insert(1, "Кількість", BigramNoSpaceCrossedCount)
column.insert(2, "Частота", BigramNoSpaceCrossedFreq)
column.insert(3, "Ентропія", BigramNoSpaceCrossedLocalEntropy)
column.to_excel(writer, 'Біграми без пробілів та з перетинами')
writer.save()

writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode = 'a')
column = pd.DataFrame(BigramNoSpaceNoCrossedLetter)
column.insert(1, "Кількість", BigramNoSpaceNoCrossedCount)
column.insert(2, "Частота", BigramNoSpaceNoCrossedFreq)
column.insert(3, "Ентропія", BigramNoSpaceNoCrossedLocalEntropy)
column.to_excel(writer, 'Біграми без пробілів та без перетинів')
writer.save()