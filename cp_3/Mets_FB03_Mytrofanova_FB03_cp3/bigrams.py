symbols = 'абвгдежзийклмнопрстуфхцчшщыьэюя'


def bigram_frequency(text, step=2):
    bigrams_frequency = {}

    for first_letter in range(0, len(text) - 1, step):
        second_letter = first_letter + 2
        if text[first_letter:second_letter] in bigrams_frequency:
            bigrams_frequency[text[first_letter:second_letter]] += 1
        else:
            bigrams_frequency[text[first_letter:second_letter]] = 0
    bigrams_number = sum(bigrams_frequency.values())

    for bigram, number in bigrams_frequency.items():
        bigrams_frequency[bigram] = round(number / bigrams_number, 8)

    return dict(sorted(bigrams_frequency.items(), key=lambda x: x[1], reverse=True))
