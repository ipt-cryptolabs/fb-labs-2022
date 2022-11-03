def count_frequencies(text):
    freq = dict()
    for i in text:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq


def count_index(text):
    text_len = len(text)
    sum_of_frequencies = 0
    for i in count_frequencies(text):
        sum_of_frequencies += i * (i - 1)
    index = 1/(text_len * (text_len - 1))
    return index


