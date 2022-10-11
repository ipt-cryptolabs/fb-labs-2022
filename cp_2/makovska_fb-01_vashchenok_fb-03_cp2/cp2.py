import re

alfavit = 'абвгдеёэжзиыйклмнопрстуфхцчшщъьюя'
alfavit_probil = 'абвгдеёэжзиыйклмнопрстуфхцчшщъьюя '


def filter_txt(file_name):
    # зчитуємо текст
    file = open(file_name, encoding="utf8")
    t = file.read()
    file.close()
    # переводимо всі літери в нижній регістр і оброблюємо
    lowered_text = t.lower()
    new_txt = re.sub(r'[^а-яё]', '',
                     lowered_text)  # прибрати всі символи, які не схожі на літери нашого алфавіту(наприкл позначення
    # переходу на новий рядок)
    # записуємо оброблений текст у файл
    new_file = open('filtered_d.txt', 'w')
    new_file.write(new_txt)
    new_file.close()


def dict_stv():
    dict_d = {}
    num = 0
    for i in alfavit:
        dict_d.update({i: num})
        num += 1
    return dict_d


def generkl_d(text, key):
    n = len(text) // len(key)
    k = len(text) % len(key)
    new_key = key * n + key[:k]
    return new_key


def ascii_cod_d(text):
    list_code = []
    d = dict_stv()
    for i in text:
        for value in d:
            if i == value:
                list_code.append(d[value])
    return list_code


def to_text_d(asciicd):
    list_code = []
    d = dict_stv()
    for i in asciicd:
        for value in d:
            if i == d[value]:
                list_code.append(value)
    return list_code


def encrypt_d(text, key):
    text = ascii_cod_d(text)
    key = ascii_cod_d(key)
    res = []
    for t, k in zip(text, key):
        let = (t + k) % 33
        res.append(let)
    return res


filter_txt('ourtext.txt')
file_d = open("filtered_d.txt")
filtered_d = file_d.read()
file_d.close()

key_d = list('аб')
gen_key_d = generkl_d(filtered_d, key_d)
cryptedlist_d = encrypt_d(filtered_d, gen_key_d)
cryptedlist_d = to_text_d(cryptedlist_d)
cryptedtext_d = ''
for i in cryptedlist_d:
    cryptedtext_d += i
#print(cryptedtext_d)
cryptfile_d = open('cryptfile_d.txt', 'w')
cryptfile_d.write(cryptedtext_d)
cryptfile_d.close()




#print

