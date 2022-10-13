from func import *

keys = ['во', 'гол', 'зола', 'баран', 'великомученник']
encr = []

with open('task1.TXT', encoding='utf-8', mode='r') as file:
    txt = file.read()

txt = clear_txt(txt)

for key in keys:
    res = encrypt(txt, key)
    encr.append(res)
    print(res, '\n')

I_list = [I(txt)]
for enc in encr:
    res = I(enc)
    I_list.append(res)

outputs = ['Відкритий', 'r = 2', 'r = 3', 'r = 4', 'r = 5', 'r = 14']
for i in range(len(outputs)):
    print(f'{outputs[i]}: {I_list[i]}', sep='\n')