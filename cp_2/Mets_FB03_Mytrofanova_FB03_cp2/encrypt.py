with open('filtered_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

periods = {'r2': 'жс', 'r3': 'хрю', 'r4': 'свин', 'r5': 'навоз', 'r10': 'радиосхема', 'r14': 'христианизация', 'r18': 'информбезопасность'}
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьъэюя'


def encrypt(text, r):
    enc_text = ""
    for i in range(len(text)):
        enc_text += alphabet[(alphabet.find(text[i]) + alphabet.find(r[i % len(r)])) % len(alphabet)]
    return enc_text


for r, value in periods.items():
    encrypted = encrypt(text, value)
    with open(f"{r}.txt", 'w', encoding='utf-8') as file:
        file.write(encrypted)

