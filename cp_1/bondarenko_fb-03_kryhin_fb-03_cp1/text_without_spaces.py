# By Bondarenko and Kryhin

FROM_FILE = 'text.txt'
TO_FILE = 'text_no_spaces.txt'

with open(FROM_FILE, 'r') as f:
    text = f.read().lower()

alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
result = ''
for i in text:
    if i in alphabet:
        result += i
    if i == 'ъ':
        result += 'ь'

with open(TO_FILE, 'w') as nf:
    nf.write(result)
