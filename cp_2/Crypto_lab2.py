import re


def hit_index_count(text):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
    letterfrequency = dict.fromkeys(alletters, 0)
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1
    frequency = []
    for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
        pct = v
        frequency.append(pct)
    hit_index = 0
    for i in frequency:
        hit_index += (i * (i + 1)) / (len(text) * (len(text) + 1))
    print(hit_index)
    return hit_index


def create_key(key, text):
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return list(("".join(key)))


def encryption(key, file):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
    ciphered_text = open("ciphered_text.txt", 'w')
    for count, symbol in enumerate(file):
        letter_index = alletters.index(symbol)
        key_index = alletters.index(key[count])
        ciphered_text.write(alletters[(letter_index + key_index) % 33])


def decryption(key, file):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
    deciphered_text = open("deciphered_text.txt", 'w')
    for count, symbol in enumerate(file):
        letter_index = alletters.index(symbol)
        key_index = alletters.index(key[count])
        deciphered_text.write(alletters[(letter_index - key_index) % 33])


# uncleantext = open("sourcetext.txt", encoding='utf-8').read()
# cleantext = re.sub('[^ А-Яа-я\nёЁ]+', '', uncleantext)
# cleantext = cleantext.replace('\n', ' ')
# cleantext = re.sub(' +', ' ', cleantext)
# cleantext = cleantext.lower()
# open('refactoredtext.txt', 'w').write(cleantext)

two_let_key = 'бу'
three_let_key = 'хог'
four_let_key = 'леон'
five_let_key = 'спайк'
big_let_key = 'отченашсущийнаенаекядвщйьмрвв'

text = open("refactoredtext.txt", 'r').read()
n=2
block_text = []
#for i in range(0,len(text),2):
    #block_text.append(i)

print(text[2::3])
#print(block_text)
encryption(create_key(big_let_key, open("ciphered_text.txt", 'r').read()), text)
decryption(create_key(big_let_key, open("ciphered_text.txt", 'r').read()), open("ciphered_text.txt", 'r').read())
# hit_index_count(open("ciphered_text.txt", 'r').read())
# hit_index_count(open("refactoredtext.txt", 'r').read())
