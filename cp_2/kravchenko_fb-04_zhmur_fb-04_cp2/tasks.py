from calc import *

with open('t1.txt', 'r', encoding='utf-8') as f:
    text = right_text(f.read())

# T1
keys = ['он', 'тор', 'маты', 'труна', 'калиййодит']
e = []

for key in keys:
    e.append(encrypt(text, key))
for en in e:
    print(en, '\n')

keys = [''] + keys
e = [text] + e

# T2
indexs = []
for en in e:
    indexs.append(Index(en))

for i in range(len(keys)):
    print(f'r = {len(keys[i])}: {indexs[i]}')

# T3
with open('t3.txt', 'r', encoding='utf-8') as f:
    t3 = right_text(f.read())

for i in range(2, 35):
    _sum = 0
    for j in range(i):
        _sum += Index(t3[j::i])
    print(f'r len = {i}: {_sum / i}')

_l = 14

vars = {'о':'', 'е':'', 'а':''}


for let in vars:
    for i in range(_l):
        vars[let] += gimmy_key(t3[i::_l], let)
    print(vars[let])

dt3 = decrypt(t3, 'экомаятникфуко')
print('\n' + dt3)
