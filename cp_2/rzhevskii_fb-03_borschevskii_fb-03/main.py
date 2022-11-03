import re
from statistics import mean


def ident_key(text, key_length):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    key = []
    for i in range(key_length):
        mostcommonletterincipher = countletterfrequency(text[i::key_length])
        curr_index = alletters.index(mostcommonletterincipher) - alletters.index('о')
        key.append(alletters[curr_index])
    # print(key)
    return ''.join(key)


def countletterfrequency(text):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    letterfrequency = dict.fromkeys(alletters, 0)
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1
    letterfrequency = dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1])))
    max_val = list(letterfrequency.keys())[0]
    # max_val = max(letterfrequency, key=letterfrequency.get)
    return max_val


def encryption(key, file, filename):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    ciphered_text = open(filename, 'w')
    for count, symbol in enumerate(file):
        letter_index = alletters.index(symbol)
        key_index = alletters.index(key[count % len(key)])
        ciphered_text.write(alletters[(letter_index + key_index) % 32])


def decryption(key, file):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    deciphered_text = open("deciphered_text.txt", 'w')
    for count, symbol in enumerate(file):
        letter_index = alletters.index(symbol)
        key_index = alletters.index(key[count % len(key)])
        deciphered_text.write(alletters[(letter_index - key_index) % 32])


def hit_index_count(text):
    alletters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    letterfrequency = dict.fromkeys(alletters, 0)
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1
    hit_index = 0
    # for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
    #     hit_index += (v * (v + 1)) / (len(text) * (len(text) + 1))
    for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
        hit_index += v * (v - 1)
    hit_index = hit_index / (len(text) * (len(text) - 1))
    # print(hit_index)
    # print(hit_index)
    # print(frequency)
    return hit_index


def guess_key_period(text, key_length):
    block_indexes = []
    for i in range(key_length):
        block_indexes.append(hit_index_count(text[i::key_length]))
    print(key_length)
    print(mean(block_indexes))
    return mean(block_indexes)


def calc_key_length(text):
    i_theory = 0.056
    allpossibilites = {}
    for i in range(2, 30):
        allpossibilites[abs((guess_key_period(text, i) - i_theory))] = i
    # print(allpossibilites)
    qqq = list(allpossibilites.keys())
    qqq.sort()
    # print('qqq   -   ' + str(qqq))
    www = []
    for i in range(len(qqq))[1:]:
        if abs(qqq[i]-qqq[i - 1]) < 0.0003:
            www.append(qqq[i - 1])
            # print(www)
        else:
            www.append(qqq[i - 1])
            break
    # print(www)
    sss = []
    if len(www) > 1:
        for i in www:
            sss.append(allpossibilites[i])
        # print(sss)
        return min(sss)
    if len(www) == 1:
        return allpossibilites[www[0]]


    # for k, v in allpossibilites.items():
    #     print(k, v)
    # return i_for_key_length.index(min(i_for_key_length, key=lambda n: (abs(i_theory - n), n)))
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

if __name__ == '__main__':
    uncleantext = open("lab_text_var4.txt", encoding='ANSI').read()
    cleantext = re.sub('[^А-Яа-я\nёЁ]+', '', uncleantext)
    cleantext = cleantext.replace('\n', '')
    cleantext = re.sub(' +', ' ', cleantext)
    cleantext = cleantext.lower()
    open('refactoredtext.txt', 'w').write(cleantext)

    two_let_key = 'бу'
    three_let_key = 'хог'
    four_let_key = 'леон'
    five_let_key = 'спайк'
    big_let_key = 'адмиралтейство'
    ref_text = open("refactoredtext.txt", 'r').read()
    print(hit_index_count(ref_text))
    # ref_text = ref_text.replace(' ', '')
    # ref_text = ref_text.replace('ё', 'е')
    # filename = '14key_ciphered.txt'
    # encryption(big_let_key, ref_text, filename)
    # cipher_text = open("ciphered_text.txt", 'r').read()
    # cipher_text = open(filename, 'r').read()

    suggestedkey = ident_key(ref_text, calc_key_length(ref_text))
    print(suggestedkey)
    # decryption('башняяростичерныемаки', cipher_text)
