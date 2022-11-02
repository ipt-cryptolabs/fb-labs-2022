import os
import glob
import matplotlib.pyplot as plt
indexes = dict()
alphabet = 'абвгдежзийклмнопрстуфхцчшщыьъэюя'


def find_index(text):
    index = 0
    for char in alphabet:
        index += text.count(char) * (text.count(char) - 1)
    index *= 1 / (len(text) * (len(text) - 1))
    return index


for file in glob.glob("*.txt"):
    if file == 'text.txt' or file == 'text_for_decr.txt':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    indexes[os.path.basename(f.name[:-4])] = find_index(text)

keys = ['r2', 'r3', 'r4', 'r5', 'r10', 'r14', 'r18', 'filtered_text']
values = [indexes[key] for key in keys]
for key in keys:
    print(key + ' index: ' + str(indexes[key]))

plt.bar(range(len(indexes)), values, align='center')
plt.xticks(range(len(indexes)), keys)
plt.show()