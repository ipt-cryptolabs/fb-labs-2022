import math
import numpy as np
import re


def inverted_element(e, mod):  # обернений елемент за модулем
    a = 1
    aa = 0
    b = 0
    bb = 1
    while (mod > 0):
        n = e // mod
        e, mod = mod, e % mod
        a, aa = aa, a - aa * n
        b, bb = bb, b - bb * n
    return a


def solving_equations(a, b, n):
    # ax = b mod n
    if (a == b == n == 0):
        print("Розв'язків не існує, так як всі елементи дорівнюють нулю")
        return None
    elif (a == 0 and b != 0):
        print("Розв'язків не існує, так як перший елемент дорівнює 0, а другий не дорівнює 0")
        return None
    elif (a != 0 and b == 0):
        return 0
    elif (a == b == 0):
        return np.arange(n)
    else:
        a = a % n
        d = math.gcd(a, n)
        ans = np.zeros(d, dtype=int)
        if (b % d == 0):
            a1 = int(a / d)
            b1 = int(b / d)
            n1 = int(n / d)
            inv = inverted_element(a1, n1)
            e0 = (b1 * inv) % n1
            for k in range(0, d):
                ans[k] = e0 + k * n1
            return ans
        else:
            print("Розв'язків не існує, так як числа", b, "та", d, "не взаємно прості")
            return None


alfavit = 'абвгдеёэжзиыйклмнопрстуфхцчшщъьюя'  # алфавіт
alfavit_d = 'абвгдежзийклмнопрстуфхцчшщьыэюя'


def filter_txt(file_name):
    # зчитуємо текст
    file = open(file_name, encoding="utf8")
    t = file.read()
    file.close()
    # переводимо всі літери в нижній регістр і оброблюємо
    lowered_text = t.lower()
    new_txt = re.sub(r'[^а-яё]', '',
                     lowered_text)  # перший аргумент - символи з якими порівнюємо, другий - якщо не співпадають, то на що замінюємо
    # записуємо оброблений текст у файл
    new_file = open('filtered.txt', 'w')
    new_file.write(new_txt)
    new_file.close()


def frequency_of_bigrams(txt, alfavit, cross=True):
    dictionary = {}  # словник зі значеннями біграма:кількість зустріваності
    freq = {}
    for l1 in alfavit:
        for l2 in alfavit:
            key = l1 + l2
            dictionary[key] = 0

    # H1 - беремо перехресні пари абвгде - аб бв вг гд ге
    if (cross == True):
        for i in range(len(txt) - 1):  # до передостанньої літери
            key = txt[i] + txt[i + 1]  # беремо 2 літери, які стоять поруч в тексті
            dictionary[key] += 1  # збільш частоту зустріваності їх пари

        for key in dictionary.keys():  # для кожної біграми (пари літер) рахуємо частоту
            freq[key] = dictionary[key] / (len(
                txt) - 1)  # -1 бо рахуємо для біграми (пари літер). типу склеїли дві літери, отримали пару і елементів стало на 1 менше
            freq[key] = round(freq[key], 6)

    # H2 - беремо кожні 2 елемента абвгде - аб вг де
    else:
        if len(txt) % 2 == 1:
            txt += "а"  # щоб кожній літері була пара
        i = 0
        for i in range(len(txt) - 1):
            if i % 2 == 1:
                continue
            key = txt[i] + txt[i + 1]
            dictionary[key] += 1  # рахуємо частоту в тексті

        for key in dictionary.keys():
            freq[key] = dictionary[key] / (len(txt) / 2)
            freq[key] = round(freq[key], 6)

    return freq


def most_freq(freq):
    a = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    return {a[n][0]: a[n][1] for n in range(5)}


filter_txt('05.txt')
file = open('filtered.txt')
text = file.read()
file.close()

f1 = frequency_of_bigrams(text, alfavit, True)
print('\nЧастота біграм: ', f1)
print(most_freq(f1))  # шукаємо 5 найбільш зустріваних
f2 = frequency_of_bigrams(text, alfavit, False)
print('\nЧастота перехресних біграм: ', f2)
print(most_freq(f2), "\n")  # шукаємо 5 найбільш зустріваних


bigrams_rus_d = ['ст', 'но', 'то', 'на', 'ен']


def clear_text(file_name):
    file = open(file_name, encoding="utf8")
    t = file.read()
    file.close()
    lowered_text = t.lower()
    new_txt = re.sub(r'[^а-яё]', '', lowered_text).rstrip().replace('ё', 'е').replace('ъ', 'ь')
    new_file = open('filtered_2.txt', 'w')
    new_file.write(new_txt)
    new_file.close()


clear_text("05.txt")
file = open('filtered_2.txt')
text_2 = file.read()
file.close()

# стандарт в ру
st = 545
no = 417
to = 572
na = 403
en = 168

# нашего шифротекста
vn = 75
tn = 571
dk = 134
un = 602
hshch = 676

a = int(solving_equations(st - en, hshch - dk, 31 ** 2))
b = int((hshch - a * st) % 31 ** 2)
print("Ваши ключи =", a, "и", b)


def convertation_to_num(bigr):
    number = alfavit_d.index(bigr[0]) * 31 + alfavit_d.index(bigr[1])
    return number


def aff_decrypt(cipher, key1, key2):
    arr_text = []
    for i in range(0, len(cipher) - 1, 2):
        x = (inverted_element(key1, 31 ** 2) * (convertation_to_num(cipher[i:i + 2]) - key2)) % (31 ** 2)
        arr_text.append(alfavit_d[x // 31] + alfavit_d[x % 31])
    str_text = ''.join(i for i in arr_text)
    return str_text


def checking(ciph):
    bukv_check = 'ое'
    pidrahunok = 0
    for bukva in text:
        pidrahunok += 1

    for c in bukv_check:
        i = 0
        for bukva in ciph:
            if c == bukva:
                i += 1
        m = i * 100 / pidrahunok
        if c == 'о' and m < 7:
            print('Если Вы видите этот текст, значит ключ не верный, так как частота o =', m, "что является меньше "
                                                                                              "стандартного.")
            return 0
        if c == 'е' and m < 7:
            print('Если Вы видите этот текст, значит ключ не верный, так как частота е =', m, "что является меньше "
                                                                                              "стандартного.")
            return 0


def main():
    key1 = a
    key2 = b
    decr = aff_decrypt(text_2, key1, key2)
    checking(decr)
    print("\nDecrypted Text: {}".format(decr))
    new_file = open('decr.txt', 'w')
    new_file.write(decr)
    new_file.close()
    print("Ваш текст записан в файл 'decr.txt'.")


main()
