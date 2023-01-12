import tools
from itertools import permutations

alpha = 'абвгдежзийклмнопрстуфхцчшщьыэюя'

file = open('04.txt')
text = tools.filter(file.read(), alpha)
file.close()

keys = []
test_keys = []

pairs = []


test_pairs = tools.bigram_analyze(*tools.bigram_xy(tools.bigram_counts(text), ['ст', 'но', 'то', 'на', 'ен'], alpha))
for i in test_pairs:
    for x, y in i.items():
        if not (x, y) in pairs:
            pairs.append((x, y))
   
pairs = list(permutations(pairs, 2))

for i in range(len(pairs)):
    k = tools.key_search(pairs[i], alpha)
    if not k in keys and not k is None:
        keys.append(k)

file = open('result.txt', 'w')
for key in keys:
    test_keys, result = tools.decrypt(key[0], key[1], 961, text, test_keys, alpha)
    if len(result) > 0:
        file.write(result)
        file.write("\n")
        file.write(str(test_keys[0]))
        file.write("\n")
        print(result)
        print(test_keys[0])

file.close()
