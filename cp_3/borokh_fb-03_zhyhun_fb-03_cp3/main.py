import pandas
import pandas as pd
import euclidean

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']


def bigrams_probability(text, step=1):  # taken from lab 1
    bigrams_dict = {}
    for i in range(0, len(text) - 1, step):
        j = i + 2
        if text[i:j] in bigrams_dict:
            bigrams_dict[text[i:j]] += 1
        else:
            bigrams_dict[text[i:j]] = 1
    bigrams_dict2 = []
    for i in bigrams_dict:
        bigrams_dict2.append((i, bigrams_dict[i] / sum(bigrams_dict.values())))
    return sorted(bigrams_dict2, key=lambda x: x[1], reverse=True)


def get_zip_from_df(df: pandas.DataFrame):
    output = []
    for i in df.columns:
        for j in df.index:
            output.append((i + j, df.loc[i, j]))
    return sorted(output, key=lambda x: x[1], reverse=True)


def biagram_number(biagram):
    global alphabet
    number = alphabet.index(biagram[0]) * len(alphabet) + alphabet.index(biagram[1])
    return number


def get_key(coded_biagrams, biagrams):
    global alphabet
    coded_diff = biagram_number(coded_biagrams[0][0]) - biagram_number(coded_biagrams[1][0])
    noncoded_diff = biagram_number(biagrams[0]) - biagram_number(biagrams[1])
    keys = euclidean.linear_comparison(coded_diff, noncoded_diff, len(alphabet) ** 2)
    ans = []
    print('keys:', keys)
    for i in keys:
        ans.append((i, (biagram_number(coded_biagrams[0][0]) -
                        i * biagram_number(biagrams[0])) % (len(alphabet) ** 2)))
    return ans


def number_biagram(number):
    global alphabet
    second = number % len(alphabet)
    first = (number - second) // len(alphabet)
    return alphabet[first] + alphabet[second]


def decryption(text, key):
    n = 0
    result = ""
    while n < len(text):
        y = biagram_number(text[n:n + 2])
        x = (euclidean.articled_element(key[0], len(alphabet) ** 2) * (y - key[1])) % (len(alphabet) ** 2)
        result += number_biagram(x)
        n += 2
    return result


if __name__ == '__main__':

    with open('09.txt', 'r', encoding='UTF-8') as f:
        text = f.read().replace('\n', '')
    with open('03.txt', 'r', encoding='UTF-8') as f:
        text1 = f.read().replace('\n', '')

    top_5_ch_03 = bigrams_probability(text1, 2)[:5]
    top_5_ch_09 = bigrams_probability(text, 2)[:5]

    lang_bigrams = get_zip_from_df(pd.read_csv('biagrams_prob.csv', index_col=0))
    top_5 = ['ст', 'но', 'то', 'на', 'ен']
 #   top_5 = [lang_bigrams[i][0] for i in range(5)]
    keys = []
    for i in range(4):
        for j in range(4):
            keys.append(get_key((top_5_ch_09[i], top_5_ch_09[i + 1]), (top_5[j], top_5[j + 1])))

    keys_ = []
    for i in keys:
        for j in i:
            keys_.append(j)
    keys_ = list(set(keys_))
    print(keys)
    for i in keys_:
        print(decryption(text1, i), end='\n')
