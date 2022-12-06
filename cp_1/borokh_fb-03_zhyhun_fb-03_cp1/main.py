# lab done by Ivan Borokh FB-03 and Zhyhun Anastasiia FB-03
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)


def letters_probability(text):
    letters_dict = {}
    for i in text:
        if i in letters_dict:
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1
    letters_dict2 = {}
    for i in letters_dict:
        letters_dict2[i] = letters_dict[i] / sum(letters_dict.values())
    return letters_dict2


def replacing(text, whitespaces=True):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
                'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']
    if whitespaces:
        alphabet.append(' ')
    text = text.replace('ё', 'е')
    text = text.replace('ъ', 'ь')
    to_delete = []
    for i in text:
        if i not in alphabet:
            to_delete.append(i)
    for i in set(to_delete):
        text = text.replace(i, '')
    return text


def bigrams_probability(text, step=1):
    bigrams_dict = {}
    for i in range(0, len(text) - 1, step):
        j = i + 2
        if text[i:j] in bigrams_dict:
            bigrams_dict[text[i:j]] += 1
        else:
            bigrams_dict[text[i:j]] = 1
    bigrams_dict2 = {}
    for i in bigrams_dict:
        bigrams_dict2[i] = bigrams_dict[i] / sum(bigrams_dict.values())

    return bigrams_dict2


def entropy_func(p_set, n=1):
    entropy = 0
    for i in p_set.keys():
        entropy += p_set[i] * np.log2(p_set[i])
    entropy = (-entropy) * (1 / n)
    return entropy


def redundancy(entropy, p_set):
    r = 1 - (entropy / np.log2(len(p_set.keys())))
    return r


def table_creator_l(letters_dict, whitespaces=True):
    columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
               'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
               'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']
    if whitespaces:
        columns.append(' ')
    df = pd.DataFrame(data=0, index=columns, columns=["Probability"])
    for i in df.index:
        if i in letters_dict:
            df["Probability"][i] += letters_dict[i]
    df = df.sort_values(by='Probability', ascending=False)
    for i in df.index:
        df["Probability"][i] = round(df["Probability"][i], 5)
    return df


def table_creator(bigram_dict, whitespaces=True):
    columns = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
               'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
               'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']
    if whitespaces:
        columns.append(' ')
    df = pd.DataFrame(data=0, index=columns, columns=columns)
    for i in df.index:
        for j in df.columns:
            if f'{i}{j}' in bigram_dict:
                df[i][j] += bigram_dict[f'{i}{j}']
            elif f'{j}{i}' in bigram_dict:
                df[j][i] += bigram_dict[f'{j}{i}']
    for i in df.index:
        for j in df.columns:
            df[i][j] = round(df[i][j], 5)
    return df


if __name__ == '__main__':
    with open('martin_plamya-i-krov-krov-drakonov_awpj-q_536484.txt', 'r', encoding='UTF-8') as file:
        text_ = file.read()
    text_ = text_.lower()
    text_ = replacing(text_)
    with open('text_with_whitespaces.txt', 'w') as f:
        f.write(text_)

    # with spaces

    letters_stats = letters_probability(text_)
    print('Table of letter`s with whitespace:')
    tabel_l = table_creator_l(letters_stats)
    print(tabel_l, '\n')
    tabel_l.to_csv('letters_w.csv')
    bigrams_stats = bigrams_probability(text_)  # intersecting bigrams
    bigrams_stats2 = bigrams_probability(text_, 2)  # non-intersecting bigrams
    print('Table of intersecting bigrams with whitespaces:')
    tabel = table_creator(bigrams_stats)
    print(tabel, '\n')
    tabel.to_csv('biagrams_w_c.csv')

    print('Table of non-intersecting bigrams with whitespaces:')
    tabel = table_creator(bigrams_stats2)
    print(tabel, '\n')
    tabel.to_csv('biagrams_w.csv')

    entropy_letters_w = entropy_func(letters_stats)

    entropy_bigrams_w = entropy_func(bigrams_stats, 2)

    entropy_bigrams_w_c = entropy_func(bigrams_stats2, 2)

    print('entropy for letters with whitespaces', entropy_letters_w)
    print("Redundancy:", redundancy(entropy_letters_w, letters_stats))
    print('entropy for intersecting bigrams with whitespaces', entropy_bigrams_w)
    print("Redundancy:", redundancy(entropy_bigrams_w, letters_stats))
    print('entropy for non-intersecting bigrams with whitespaces', entropy_bigrams_w_c)
    print("Redundancy:", redundancy(entropy_bigrams_w_c, letters_stats), '\n')

    # without spaces

    text_ = replacing(text_, whitespaces=False)
    with open('text_without_whitespaces.txt', 'w') as f:
        f.write(text_)

    letters_stats = letters_probability(text_)
    print('Table of letter`s without whitespace:')
    tabel_l = table_creator_l(letters_stats, False)
    print(tabel_l, '\n')
    tabel_l.to_csv('letters.csv')
    bigrams_stats = bigrams_probability(text_)  # intersecting bigrams
    bigrams_stats2 = bigrams_probability(text_, 2)  # non-intersecting bigrams
    print('Table of intersecting bigrams without whitespaces:')
    tabel = table_creator(bigrams_stats, False)
    print(tabel, '\n')
    tabel.to_csv('biagrams_c.csv')

    print('Table of non-intersecting bigrams without whitespaces:')
    tabel = table_creator(bigrams_stats2, False)
    print(tabel, '\n')
    tabel.to_csv('biagrams.csv')

    entropy_letters = entropy_func(letters_stats)

    entropy_bigrams = entropy_func(bigrams_stats, 2)

    entropy_bigrams_c = entropy_func(bigrams_stats2, 2)

    print('entropy for letters without whitespaces', entropy_letters)
    print("Redundancy:", redundancy(entropy_letters, letters_stats))
    print('entropy for intersecting bigrams without whitespaces', entropy_bigrams)
    print("Redundancy:", redundancy(entropy_bigrams, letters_stats))
    print('entropy for non-intersecting bigrams without whitespaces', entropy_bigrams_c)
    print("Redundancy:", redundancy(entropy_bigrams_c, letters_stats))
