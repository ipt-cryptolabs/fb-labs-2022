from func import *

with open('encrypted8.txt', encoding='utf-8', mode='r') as f:
    txt = f.read()

df = pd.read_excel('lab1.xlsx', sheet_name='Моногр без пробілів', index_col=0)
print(f'Theory: {MI(df)}')

txt = clear_txt(txt)


for i in range (2, 35):
    summ = 0
    for j in range(i):
        summ += I(txt[j::i])
    print(f'r len = {i}: {summ / i}')


r = 20

for i in range(20):
    print(guess_key(txt[i::r], 'о'), guess_key(txt[i::r], 'е'), guess_key(txt[i::r], 'а'), guess_key(txt[i::r], 'и'), guess_key(txt[i::r], 'н'))

decr_txt = decrypt(txt, 'улановсеребряныепули')
with open('decrypted8.txt', encoding='utf-8', mode='w') as file:
    file.write(decr_txt)

