import re
import math

alfavit = 'абвгдеёэжзиыйклмнопрстуфхцчшщъьюя'
alfavit_probil = 'абвгдеёэжзиыйклмнопрстуфхцчшщъьюя '


def filter_txt(file_name):
    # зчитуємо текст
    file = open(file_name, encoding="utf8")
    t = file.read()
    file.close()
    # переводимо всі літери в нижній регістр і оброблюємо
    lowered_text = t.lower()
    new_txt = re.sub(r'[^а-яё ]', '', lowered_text)  # прибрати всі символи, які не схожі на літери нашого алфавіту(наприкл позначення переходу на новий рядок \n)
    # записуємо оброблений текст у файл
    new_file = open('filtered_d.txt', 'w')
    new_file.write(new_txt)
    new_file.close()
    

filter_txt('ourtext.txt')
file_d = open("filtered_d.txt")
filtered_d = file_d.read()
file_d.close()














#print

