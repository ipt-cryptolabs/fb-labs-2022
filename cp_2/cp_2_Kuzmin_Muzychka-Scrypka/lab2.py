from collections import Counter
from distutils.ccompiler import new_compiler
from re import A

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

# Шифруємо текст
def vizhenera(key, oldfile, alphabet):
    new_file = ''
    value = 0
    for i in oldfile:
        new_index = (alphabet.find(i) + alphabet.find(key[value])) % len(alphabet)
        value = (value + 1) % len(key)
        new_file += alphabet[new_index]
    return new_file

# Шукаємо індекс
def find_index(new_complite):
    count_index = Counter(new_complite)
    sum_index = 0
    for i in count_index.values():
        sum_index += (i * (i - 1))
    sum_index /= (len(new_complite) * (len(new_complite) - 1))    
    return sum_index

# Очищуємо текст
def cleaner(alphabet, oldfile):
    oldfile = oldfile.lower()
    oldfile = oldfile.replace('ё', 'е')
    clean_file = ''
    for i in oldfile:
        if i in alphabet:
            clean_file += i
    return clean_file

# Пошук теоретичного ключа
def select_key(descriription_taks_file, aeo):
    count_firstly = Counter(descriription_taks_file)
    key = ''
    max_count = max(count_firstly.values())
    for i in count_firstly.keys(): # кожен ітератор- це ключ
        if count_firstly[i] == max_count: # тут отримується значення, яке й знаходиться завдяки даному ключу
           key = i # тут записується value, що співпав з максимальним числом
    answer_key = (alphabet.find(key) - alphabet.find(aeo)) % 32 # 0(а) / 5(е) / 14(o)
    return alphabet[answer_key]

# Підстановка ключа та спроба розшифровування
def complite_text(descriription_taks_file, key_list_deciphered, alphabet):
    deciphered_file = ''
    num_key = 0
    len_key = len(key_list_deciphered)
    for char_in_file in descriription_taks_file:
        key_x = alphabet.find(key_list_deciphered[num_key])
        num_index = ((alphabet.find(char_in_file) - key_x) % 32)
        deciphered_file += alphabet[num_index]  
        num_key = (num_key + 1) % len_key
    return deciphered_file

# Задаємо ключі для шифрування, очищуємо текст та запускаємо функцію шифрування
key_list = ['фи', 'физ', 'физк', 'физке', 'физкеклучшевсех']
with open('file.txt', encoding='utf-8') as file:
    oldfile = file.read()
oldfile = cleaner(alphabet, oldfile)
new_complite = []
for key in key_list:
    new_complite.append(vizhenera(key, oldfile, alphabet))

# Знаходження індексів
# print('\n Індекс \n')
# print(find_index(oldfile))
# print('Знаходимо всі індекси')
#for i in new_complite:
#   print(find_index(i))

print('\n')

# Файл для розшифровування
with open('variant_file.txt', encoding='utf-8', mode='r') as variant_file:
    descriription_taks_file = variant_file.read()
descriription_taks_file = cleaner(alphabet, descriription_taks_file)

# Знаходження розміру ключа
# for i in range(2, 36):
#     sum_index = 0
#     for j in range(0, i):
#         sum_index += find_index(descriription_taks_file[j::i])
#     print(f'{sum_index / i}  i =  {i} ')   

# Знаходження теоретичних ключів
key_list_e = []
key_list_o = []
key_list_a = []
key_len = 15
for i in range(0,key_len):
    key_list_e.append(select_key(descriription_taks_file[i::key_len], 'е'))
    key_list_o.append(select_key(descriription_taks_file[i::key_len], 'о'))
    key_list_a.append(select_key(descriription_taks_file[i::key_len], 'а'))

# Розшифрований файл
# print(complite_text(descriription_taks_file, key_list_o, alphabet))
# for i in key_list_e:
#     print(i, end="")
# print('\n')    
# for i in key_list_o:
#     print(i, end="")
# print('\n')
# for i in key_list_a:
#     print(i, end="")

key_yes_yes_yes = 'крадущийсявтени'
print(complite_text(descriription_taks_file, key_yes_yes_yes, alphabet))

print('\n')