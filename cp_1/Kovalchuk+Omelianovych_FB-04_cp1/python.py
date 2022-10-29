import re
from collections import Counter
import pandas as pd
import math


def clear_text(raw_text):
    with open(raw_text, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    text = re.sub("[^а-я]", " ", text)
    text = text.replace("ё", "е")

    while "  " in text:
        text = text.replace("  ", " ")

    with open("clear_text.txt", 'w', encoding='utf-8') as file:
        file.write(text)


def clear_spaces(text_with_spaces):
    with open(text_with_spaces, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.replace(" ", "")

    with open("withoutspaces.txt", 'w', encoding='utf-8') as file:
        file.writelines(text)


def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    return text


def count_letters_with_spaces(text):
    dict = Counter(text)
    frequencies = []
    for i in dict.keys():
        frequencies.append(dict[i] / len(text))

    entropys = []
    for i in frequencies:
        entropys.append(-(i * math.log2(i)))

    writer = pd.ExcelWriter('result.xlsx', engine='xlsxwriter')
    df = pd.DataFrame(dict.keys())
    df.insert(1, "Кількість", dict.values())
    df.insert(2, "Частоти", frequencies)
    df.insert(3, "Ентропії", entropys)
    df.to_excel(writer, 'Моногр з пробіл')
    writer.save()


def count_letters_without_spaces(text):
    dict = Counter(text)
    frequencies = []
    for i in dict.keys():
        frequencies.append(dict[i] / len(text))

    entropys = []
    for i in frequencies:
        entropys.append(-(i * math.log2(i)))

    writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode='a')
    df = pd.DataFrame(dict.keys())
    df.insert(1, "Кількість", dict.values())
    df.insert(2, "Частоти", frequencies)
    df.insert(3, "Ентропії", entropys)
    df.to_excel(writer, 'Моногр без пробіл')
    writer.save()


def count_bigrams_with_spaces(text):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е',
                'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы',
                'э', 'ю', 'я', ' ']

    list0 = []
    list1 = []

    for i in alphabet:
        for k in alphabet:
            list0.append(k + i)
            list1.append(text.count(k + i))


    frequencies = []
    for i in range(len(list0)):
        frequencies.append(list1[i] / sum(list1))

    entropys = []
    for i in frequencies:
        if i != 0:
            entropys.append(-(i * math.log2(i)))
        else:
            entropys.append(0)

    writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode='a')
    df = pd.DataFrame(list0)
    df.insert(1, "Кількість", list1)
    df.insert(2, 'Частота', frequencies)
    df.insert(3, 'ентропії', entropys)
    df.to_excel(writer, 'Біграми з перетинами і пробіл')
    writer.save()


def count_bigrams_without_spaces(text):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е',
                'ж', 'з', 'и', 'й', 'к', 'л', 'м',
                'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы',
                'э', 'ю', 'я']

    list0 = []
    list1 = []

    for i in alphabet:
        for k in alphabet:
            list0.append(k + i)
            list1.append(text.count(k + i))

    frequencies = []
    for i in range(len(list0)):
        frequencies.append(list1[i] / sum(list1))

    entropys = []
    for i in frequencies:
        if i != 0:
            entropys.append(-(i * math.log2(i)))
        else:
            entropys.append(0)

    writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode='a')
    df = pd.DataFrame(list0)
    df.insert(1, "Кількість", list1)
    df.insert(2, 'Частота', frequencies)
    df.insert(3, 'ентропії', entropys)
    df.to_excel(writer, 'Біграми з перетинами без пробіл')
    writer.save()


def count_bigrams_without_intersection_with_spaces(text):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е',
            'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы',
            'э', 'ю', 'я', ' ']

    list0 = []

    for i in alphabet:
        for k in alphabet:
            list0.append(k + i)

    dict0 = {i:0 for i in list0}

    i = 0
    while i < len(text):
        bigram = text[i:i+2]
        dict0[bigram] += 1
        i += 2

    dictValues = list(dict0.values())
    frequencies = []
    for i in range(len(dict0)):
        frequencies.append(dictValues[i] / sum(dict0.values()))

    entropys = []
    for i in frequencies:
        if i != 0:
            entropys.append(-(i * math.log2(i)))
        else:
            entropys.append(0)

    writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode='a')
    df = pd.DataFrame(list0)
    df.insert(1, "Кількість", dict0.values())
    df.insert(2, 'Частота', frequencies)
    df.insert(3, 'ентропії', entropys)
    df.to_excel(writer, 'Біграм без перет з пробіл')
    writer.save()


def count_bigrams_without_intersection_without_spaces(text):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е',
            'ж', 'з', 'и', 'й', 'к', 'л', 'м',
            'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы',
            'э', 'ю', 'я']

    list0 = []

    for i in alphabet:
        for k in alphabet:
            list0.append(k + i)

    dict0 = {i:0 for i in list0}

    i = 0
    while i < len(text):
        bigram = text[i:i+2]
        dict0[bigram] += 1
        i += 2

    dictValues = list(dict0.values())
    frequencies = []
    for i in range(len(dict0)):
        frequencies.append(dictValues[i] / sum(dict0.values()))

    entropys = []
    for i in frequencies:
        if i != 0:
            entropys.append(-(i * math.log2(i)))
        else:
            entropys.append(0)

    writer = pd.ExcelWriter('result.xlsx', engine='openpyxl', mode='a')
    df = pd.DataFrame(list0)
    df.insert(1, "Кількість", dict0.values())
    df.insert(2, 'Частота', frequencies)
    df.insert(3, 'ентропії', entropys)
    df.to_excel(writer, 'Біграм без перес без пробіл')
    writer.save()


clear_text("text.txt")
text = readfile("clear_text.txt")
clear_spaces("clear_text.txt")
text_without_spaces = readfile("withoutspaces.txt")

count_letters_with_spaces(text)
count_letters_without_spaces(text_without_spaces)
count_bigrams_with_spaces(text)
count_bigrams_without_spaces(text_without_spaces)
count_bigrams_without_intersection_with_spaces(text)
count_bigrams_without_intersection_without_spaces(text_without_spaces)