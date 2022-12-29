print("Task 1")

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

key_0 = "эь"
key_1 = "нрм"
key_2 = "дзкц"
key_3 = "яюьен"
key_jestkiy = "жесткийключдлятру"

with open('finaltext.txt', 'r', encoding='utf-8') as file:
    text = file.read()


def vigener_chel(plain_text, key, alphabet):
    m = len(alphabet)
    cr = ""
    for i in range(len(plain_text) - 1):
        cr += f"{alphabet[(alphabet.find(plain_text[i]) + alphabet.find(key[i % len(key)])) % m]}"
    return cr


CT = []
for key in (key_0, key_1, key_2, key_3, key_jestkiy):
    print(f"Ключ довжини {len(key)}, {key}:")
    CT.append(vigener_chel(text, key, alphabet))
    print(CT[-1])


print("Task 2")


def super_index(text: str, alphabet):
    an = 0
    n = len(text)
    for i in alphabet:
        an += (text.count(i)) * (text.count(i) - 1)

    return an/(n * (n - 1))

n = 2
for i in CT:
    if n == 6:
        n = 17
    print(f"Ключ довжини {n}:")
    n += 1
    print(super_index(i, alphabet))

print("Відкритий текст:")
print(super_index(text, alphabet))

print("Task 3")

with open('encoding.txt', 'r', encoding='utf-8') as file:
    text = file.read()


def rozbivka_na_gramy(text: str, n, stop):
    temp = []
    for i in range(n):
        j = i
        l = ""
        while j < len(text):
            l += text[j]
            j += n
        temp.append(l)

    if stop:
        return temp

    k = 0
    for i in temp:
        k += super_index(i, alphabet)
    return k/n


def find_most_common(text: str, alphabet):
    temp = []
    for i in alphabet:
        temp.append(text.count(i))
    return temp.index(max(temp))

for i in range(2,40):
    print(rozbivka_na_gramy(text, i, False))

r = 16

a = rozbivka_na_gramy(text, r, True)
solved_keys = []
for i in a:
    y1 = find_most_common(i, alphabet)
    x1 = 14
    solved_keys.append(alphabet[((y1 - x1) % 32)])

key = ''.join(solved_keys)
print(key)
new_text, num = '', 0
while num < len(text):
    new_text += alphabet[(alphabet.find(text[num]) - alphabet.find(key[num % r]))%32]
    num += 1
print(new_text)

with open('decoding.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)


