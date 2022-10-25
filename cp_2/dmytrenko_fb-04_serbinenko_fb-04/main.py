file = open('se.txt').read().lower().replace('\n', '').replace(' ', '').replace('ё', 'е').replace('ъ', 'ь')
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя '

txt = ''
for i in file:
    if i in alphabet:
        txt += i

print(txt)

with open('pt.txt', 'w') as file:
    file.write(txt)
