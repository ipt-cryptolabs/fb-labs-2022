with open('19.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text.lower()

a = 'абвгдежзийклмнопрстуфхцчшщыьэюя'
print(len(a))
answer = ''
for i in text:
    if i in a:
        answer += i
    if i == '\n':
        answer += ''
    if i == 'ъ':
         answer += 'ь'
    if i == 'ё':
        answer += 'е'

answer = ' '.join(list(answer.split()))

with open('finaltext.txt', 'w', encoding='utf-8') as file:
    file.write(answer)