alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
keylist = ['нв', 'при', 'гукф', 'холмс', 'семестровыйконтроль']


def text_with_spaces(file_input, file_output):
    with open(file_input, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = text.replace('ё', 'е').replace('ъ', 'ь').replace('\n', '').replace('  ', ' ').replace(' ', '')
    result = ''
    for i in text:
        if i in alphabet:
            result += i
    with open(file_output, 'w', encoding='utf-8') as file:
        file.write(result)


text_with_spaces('text.txt', 'filtered_text.txt')

text = open('filtered_text.txt', encoding='utf-8').read()


def encrypt(text, key):
    result = ''
    i = 0
    for value in text:
        key_index = i % len(key)
        result = result + alphabet[(alphabet.index(value) + alphabet.index(key[key_index])) % len(alphabet)]
        i += 1
    return result


def decrypt(file, key):
    result = ''
    i = 0
    for value in file:
        key_index = i % len(key)
        result = result + alphabet[(alphabet.index(value) - alphabet.index(key[key_index])) % len(alphabet)]
        i += 1
    return result


def index(file):
    result = 0
    i = 0
    while i < len(alphabet):
        letters = file.count(alphabet[i])
        result += (letters - 1) * letters
        i += 1
    result *= 1/((len(text)-1) * len(text))

    return result

print('Обраний текст:\n', text)
print(f'Індекс відповідності: {index(text)}')

for key in keylist:
    encrypted_text = encrypt(text, key)
    print('Зашифрований текст шифром', key, ':\n', encrypted_text)
    print(f'Індекс відповідності: {index(encrypted_text)}')


encrypted_file2 = open('encrypted2.txt', encoding='utf-8').read()
print('Перевірка правильності розшифруванням:\n', decrypt(encrypted_file2, keylist[0]))



