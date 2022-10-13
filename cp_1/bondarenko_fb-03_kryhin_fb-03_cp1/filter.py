# By Bondarenko and Kryhin

FROM_FILE = 'text.txt'
TO_FILE = 'new_text.txt'
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя '

with open(FROM_FILE, 'r') as f:
    text = f.read().lower()

result = ''
for i in text:
    if i in alphabet:
        result += i
    if i == '\n':
        result += ' '
    if i == 'ъ':
        result += 'ь'

with open(TO_FILE, 'w') as nf:
    nf.write(" ".join(result.split()))
