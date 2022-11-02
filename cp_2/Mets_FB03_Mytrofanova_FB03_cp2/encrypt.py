with open('filtered_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

periods = {'r2': 'жс', 'r3': 'хрю', 'r4': 'негр', 'r5': 'навоз', 'r10': 'черножопый', 'r14': 'христианизация', 'r18': 'информбезопасность'}
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьэюя'


def encrypt(text, r):
    enc_text = ""
    int_key = [text.find(i) for i in r]
    for i in range(len(text)):
        enc_text += text[(i + int_key[i % len(r)]) % len(alphabet)]
    return enc_text


for r, value in periods.items():
    encrypted = encrypt(text, value)
    with open(f"{r}.txt", 'w', encoding='utf-8') as file:
        file.write(encrypted)

