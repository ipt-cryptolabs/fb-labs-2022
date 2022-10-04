import codecs
import math

import openpyxl
import pandas
import xlsxwriter

alphabet_32 = {"а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
               "х",
               "ц", "ч", "ш", "щ", "ы", "ь", "э", "ю", "я", " "}
alphabet_31 = {"а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
               "х",
               "ц", "ч", "ш", "щ", "ы", "ь", "э", "ю", "я"}


def ocr(dictionary_ocr, alph, text):
    sum = 0
    for letter in alph:
        dictionary_ocr[letter] = text.count(letter)
        sum += dictionary_ocr[letter]
    return sum


def apr(dictionary_apr, dictionary_ocr, alph, sum):
    for letter in alph:
        dictionary_apr[letter] = dictionary_ocr[letter] / sum


def ngramma(dictionary_apr):
    ngram = 0
    for letter in dictionary_apr:
        if dictionary_apr[letter] != 0:
            ngram -= (dictionary_apr[letter] * math.log(dictionary_apr[letter], 2))
    return ngram


def toexl(dictionary_apr, entr, redun, name):
    col1 = "Алфавіт"
    col2 = "Ймовірність"
    col3 = "Результати"
    arr1 = []
    arr2 = []
    for letter in dictionary_apr:
        arr1.append(letter)
        arr2.append(dictionary_apr[letter])
    arr3 = ["Ентропія", entr, "Надлишковість", redun]
    for i in range(4, len(arr1),1):
        arr3.append(" ")
    data = pandas.DataFrame({col1: arr1, col2: arr2, col3: arr3})
    with pandas.ExcelWriter("results.xlsx", mode="a", engine="openpyxl") as writer:
        data.to_excel(writer, sheet_name=name, index=False)





def func(alph, text, n, name):
    dictionary_ocr = {}
    dictionary_apr = {}
    sum = 0
    sum = ocr(dictionary_ocr, alph, text)
    apr(dictionary_apr, dictionary_ocr, alph, sum)
    entrop = 1 / n * ngramma(dictionary_apr)
    red = 1 - (entrop / math.log(len(alph), 2))
    toexl(dictionary_apr, entrop, red, name)
    return entrop


def alph_wht_step_n(text, n):
    alph = []
    for i in range(0, len(text) - n, n):
        temp = text[i] + text[i + 1]
        if temp not in alph:
            alph.append(temp)
    return alph


def redun(entr, alphabet):
    return 1 - (entr / math.log(len(alphabet), 2))


file = codecs.open("Vedmak.txt", "r", "utf_8_sig")  # читаємо рос текст
text = file.read()  # відриваємо файл
file.close()

text = text.replace("\n", " ")  # видаляємо переноси

line = "".join(c for c in text if c.isalpha() or c == " ")  # видаляємо зайві символи
line = " ".join(line.split())
line = line.lower()

text = ""
for letter in line:
    if letter == "ё":
        text += "е"
    elif letter == "ъ":
        text += "ь"
    elif letter in alphabet_32:
        text += letter

text_1 = "".join(text.split())  # текст без пробілів

#writer = pandas.ExcelWriter('results.xlsx', engine='xlsxwriter')
#writer.save()
book = xlsxwriter.Workbook("results.xlsx")
sheet = book.add_worksheet()
sheet.write(0,0,"Комп'ютерний практикум 1")
sheet.write(0,1,"Павелко Володимир")
sheet.write(0,2,"Бочок Олександра")
book.close()


# 1n wth spaces
onegrama_wth_sp = func(alphabet_32, text, 1, "1n wth spaces")
print(onegrama_wth_sp)

redundancy_wth_sp = redun(onegrama_wth_sp, alphabet_32)
print(redundancy_wth_sp)

# 1n wthout spaces
onegrama_wthout_sp = func(alphabet_31, text, 1, "1n wthout spaces")
print(onegrama_wthout_sp)

redundancy_wthout_sp = redun(onegrama_wthout_sp, alphabet_31)
print(redundancy_wthout_sp)

# 2n wth spaces step = 1
alphabet_step1_wth_sp = alph_wht_step_n(text, 1)
bigrama_step1_wth_sp = func(alphabet_step1_wth_sp, text, 2, "2n wth spaces step = 1")
print(bigrama_step1_wth_sp)

redundancy_step1_wth_sp = redun(bigrama_step1_wth_sp, alphabet_step1_wth_sp)
print(redundancy_step1_wth_sp)

# 2n wthout spaces step = 1
alphabet_step1_wthout_sp = alph_wht_step_n(text_1, 1)
bigrama_step1_wthout_sp = func(alphabet_step1_wthout_sp, text_1, 2, "2n wthout spaces step = 1")
print(bigrama_step1_wthout_sp)

redundancy_step1_wthout_sp = redun(bigrama_step1_wthout_sp, alphabet_step1_wthout_sp)
print(redundancy_step1_wthout_sp)

# 2n wth spaces step = 2
alphabet_step2_wth_sp = alph_wht_step_n(text, 2)
bigrama_step2_wth_sp = func(alphabet_step2_wth_sp, text, 2, "2n wth spaces step = 2")
print(bigrama_step2_wth_sp)

redundancy_step2_wth_sp = redun(bigrama_step2_wth_sp, alphabet_step2_wth_sp)
print(redundancy_step2_wth_sp)

# 2n wthout spaces step = 2
alphabet_step2_wthout_sp = alph_wht_step_n(text_1, 2)
bigrama_step2_wthout_sp = func(alphabet_step2_wthout_sp, text_1, 2, "2n wthout spaces step = 2")
print(bigrama_step2_wthout_sp)

redundancy_step2_wthout_sp = redun(bigrama_step2_wthout_sp, alphabet_step2_wthout_sp)
print(redundancy_step2_wthout_sp)

