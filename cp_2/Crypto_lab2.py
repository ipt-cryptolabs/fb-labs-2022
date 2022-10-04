import re
from statistics import mean


def ident_key(text, key_length):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    key = []
    for i in range(key_length):
        key.append(alletters[abs(alletters.index('о') - alletters.index(
            list(countletterfrequency(text[i::key_length]).keys())[0]))])
    print(key)
    return key


def countletterfrequency(text):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    letterfrequency = dict.fromkeys(alletters, 0)
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1
    max_val = max(letterfrequency.values())
    final_dict = {k: v for k, v in letterfrequency.items() if v == max_val}
    return final_dict


def hit_index_count(text):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
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
    # print(hit_index)
    # print(frequency)
    return hit_index


def create_key(key, text):
    key = list(key)
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


def guess_key_period(text, key_length):
    block_indexes = []
    for i in range(key_length):
        block_indexes.append(hit_index_count(text[i::key_length]))
    return mean(block_indexes)


def calc_key_length(text):
    # ref_text = open("refactoredtext.txt", 'r').read()
    I_THEORY = 0.066
    I_for_key_length = []
    number = 0
    for i in range(2, 15):
        I_for_key_length.append(guess_key_period(text, i))
    return I_for_key_length.index(min(I_for_key_length, key=lambda n: (abs(I_THEORY - n), n))) + 2
    # print(I_for_key_length)
    # return I_for_key_length
    # print(I_for_key_length.index(number))
    # return I_for_key_length.index(number)


# uncleantext = open("lab_text.txt", encoding='utf-8').read()
# cleantext = re.sub('[^ А-Яа-я\nёЁ]+', '', uncleantext)
# cleantext = cleantext.replace('\n', '')
# cleantext = re.sub(' +', ' ', cleantext)
# cleantext = cleantext.lower()
# open('lab_text_refactored.txt', 'w').write(cleantext)

two_let_key = 'бу'
three_let_key = 'хог'
four_let_key = 'леон'
five_let_key = 'спайк'
big_let_key = 'отченашсущийнаенаекядвщйьмрвв'
ref_text = open("refactoredtext.txt", 'r').read()

encryption(create_key(five_let_key, ref_text), ref_text)
cipher_text = open("ciphered_text.txt", 'r').read()
print(ident_key(cipher_text, calc_key_length(cipher_text)))
# lab_text = open("lab_text_refactored.txt", 'r').read()
# print(calc_key_length(cipher_text))

