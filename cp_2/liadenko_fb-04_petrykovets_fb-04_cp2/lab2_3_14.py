from func import *

with open('encrypted14.txt', encoding='utf-8', mode='r') as f:
    txt = f.read()

df = pd.read_excel('lab1.xlsx', sheet_name='Моногр без пробілів', index_col=0)
print(f'Theory: {MI(df)}')

txt = clear_txt(txt)


for i in range (2, 35):
    summ = 0
    for j in range(i):
        summ += I(txt[j::i])
    print(f'r len = {i}: {summ / i}')


r = 19

for i in range(r):
    print(guess_key(txt[i::r], 'о'), guess_key(txt[i::r], 'е'), guess_key(txt[i::r], 'а'), guess_key(txt[i::r], 'и'), guess_key(txt[i::r], 'н'), guess_key(txt[i::r], 'т'))

decr_txt = decrypt(txt, 'конкистадорыгермеса')
with open('decrypted14.txt', encoding='utf-8', mode='w') as file:
    file.write(decr_txt)

