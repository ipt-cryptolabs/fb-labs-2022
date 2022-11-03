import matplotlib.pyplot as plt
import pandas as pd

alphabet_ = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
             'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def letters_probability(text):
    letters_dict = {}
    for i in text:
        if i in letters_dict:
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1
    return letters_dict


def de_chiffre_de_vigenere(text: str, chif: str):
    global alphabet_

    out_text = ''
    for i in range(len(text)):
        new_let = (alphabet_.index(text[i]) - (alphabet_.index(chif[i % len(chif)])) + 32) % len(alphabet_)
        out_text += alphabet_[new_let]
    return out_text


def chiffre_de_vigenere(text: str, chif: str):
    global alphabet_

    out_text = ''
    for i in range(len(text)):
        new_let = (alphabet_.index(text[i]) + (alphabet_.index(chif[i % len(chif)]))) % len(alphabet_)
        out_text += alphabet_[new_let]
    return out_text


def compliance_index(text: str, letters: dict):
    global alphabet_

    stats = 0
    for i in letters.keys():
        stats += letters[i] * (letters[i] - 1)
    return (1 / (len(text) * (len(text) - 1))) * stats


def break_for_blocks(text: str, r: int):
    global ot_ci
    blocks = [''] * r
    for i in range(len(text)):
        blocks[i % r] += text[i]
    i_s = [compliance_index(i, letters_probability(i)) for i in blocks]
    return abs(sum(i_s) / r - ot_ci)


def break_for_blocks_(text: str, r: int):
    blocks = [''] * r
    for i in range(len(text)):
        blocks[i % r] += text[i]
    return blocks


if __name__ == '__main__':
    with open('text_1.txt', 'r', encoding='UTF-8') as f:
        text = f.read().replace('\n', '')
    text = text.replace('ё', 'е')
    text = text.replace(' ', '')

    encrypted_text_2 = chiffre_de_vigenere(text, 'до')
    encrypted_text_3 = chiffre_de_vigenere(text, 'дом')
    encrypted_text_4 = chiffre_de_vigenere(text, 'домд')
    encrypted_text_5 = chiffre_de_vigenere(text, 'домдр')
    encrypted_text_11 = chiffre_de_vigenere(text, 'домдраконов')

    #    decrypted_text_2 = decryption(text,)

    with open('en_text_2.txt', 'w') as f:
        f.write(encrypted_text_2)
    with open('en_text_3.txt', 'w') as f:
        f.write(encrypted_text_3)
    with open('en_text_4.txt', 'w') as f:
        f.write(encrypted_text_4)
    with open('en_text_5.txt', 'w') as f:
        f.write(encrypted_text_5)
    with open('en_text_11.txt', 'w') as f:
        f.write(encrypted_text_11)

    ot_ci = compliance_index(text, letters_probability(text))  # 0
    et2_ci = compliance_index(encrypted_text_2, letters_probability(encrypted_text_2))  # 2
    et3_ci = compliance_index(encrypted_text_3, letters_probability(encrypted_text_3))  # 3
    et4_ci = compliance_index(encrypted_text_4, letters_probability(encrypted_text_4))  # 4
    et5_ci = compliance_index(encrypted_text_5, letters_probability(encrypted_text_5))  # 5
    et11_ci = compliance_index(encrypted_text_11, letters_probability(encrypted_text_11))  # 11

    """    
    print(ot_ci)
    print(et2_ci)
    print(et3_ci)
    print(et4_ci)
    print(et5_ci)
    print(et11_ci)
    """

    array = [ot_ci, et2_ci, et3_ci, et4_ci, et5_ci, et11_ci]
    indexes = [0, 2, 3, 4, 5, 11]

    plt.plot(indexes, array)
    plt.scatter(indexes, array, marker='*')
    plt.grid(which='major', color='k')
    plt.minorticks_on()
    plt.grid(which='minor', color='gray', linestyle=':')

    plt.show()

    with open('text_2.txt', 'r', encoding='UTF-8') as f:
        text1 = f.read()
    text1 = text1.replace('\n', '')

    indexes = {}
    for i in range(2, 31):
        indexes[i] = break_for_blocks(text1, i)

    plt.bar(range(len(indexes)), list(indexes.values()), align='center')
    plt.xticks(range(len(indexes)), list(indexes.keys()))
    plt.show()

    max_r = min(indexes.values())
    for key, value in indexes.items():
        if value == max_r:
            print(key)
            break
    key_blocks = break_for_blocks_(text1, 21)
    cr_key = ''
    for i in key_blocks:
        probs = letters_probability(i)
        max_repeted = max(probs.values())
        for key, value in probs.items():
            if value == max_repeted:
                cr_key += key
    df = pd.read_csv('letters.csv')
    for j in df['letters'].values:
        answer = ''
        for k in cr_key:
            key = (alphabet_.index(k) - alphabet_.index(j)) % 32
            answer += alphabet_[key]
        print(answer)
