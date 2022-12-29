import re
import itertools
import math
import csv


alletters1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
              'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
              'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def cleantextfunc(sourcefile, outputfile):
    """Function creates new txt file with cleaned text(only spaces and lowercase chars left)

    Parameters
    ----------
    sourcefile : str
        txt file with source text

    outputfile : str
        Name of the file where reformatted text should be stored
    """
    sourcetext = open(sourcefile, encoding='utf-8').read()
    cleantext = re.sub('[^ А-Яа-я\nёЁ]+', '', sourcetext)
    cleantext = cleantext.replace('\n', ' ')
    cleantext = re.sub(' +', ' ', cleantext)
    cleantext = cleantext.lower()
    open(outputfile, 'w').write(cleantext)


def countletterfrequency(spaces=False):
    """Function counts the probablitiy of occurence for every character in text
    and returns the list of all probabilities in descending order in a list.
    Prints all the letters with it's corresponding value in console

    Parameters
    ----------
    spaces : bool
        Whether we include spaces in text or not. By default false

    Returns
    -------
    list
        a list of all the probablities in descending order
    """
    alletters = alletters1
    text = open("refactoredtext.txt").read()
    if spaces is True:
        alletters.append(' ')
    letterfrequency = dict.fromkeys(alletters, 0)
    for i in text:
        if i in alletters:
            letterfrequency[i] += 1

    # header = ['Letter', 'Frequency']
    # with open('singleletters_nospace.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     for items in reversed(sorted(letterfrequency.items(), key=lambda item: item[1])):
    #         print(items)
    #         writer.writerow(items)

    percentages = []
    totaloccurences = sum(letterfrequency.values())
    for k, v in dict(reversed(sorted(letterfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 3)
        print(k, str(pct))
        percentages.append(pct)
    return percentages


def countbigrams(spaces=False, overlapping=True):
    """Function counts probablitiy of occurence for every bigram in text
    and returns the list of all probabilities in descending order.
    Prints all the bigrams with it's corresponding value in console

    Parameters
    ----------
    spaces : bool
        Whether we include spaces in text or not. By default false
    overlapping : bool
        Whether we count overlapping bigrams. By default true

    Returns
    -------
    list
        a list of all the probablities in descending order
    """
    alletters = alletters1
    if overlapping is True:
        step = 1
    else:
        step = 2

    text = open("refactoredtext.txt").read()
    allbigrams = []
    if spaces is True:
        alletters.append(' ')
        templist = [alletters, alletters]
    else:
        templist = [alletters, alletters]
        text = text.replace(' ', '')
    for element in itertools.product(*templist):
        allbigrams.append(''.join(element))

    bigramfrequency = dict.fromkeys(allbigrams, 0)
    for i in range(0, len(text) - 1, step):
        bigramfrequency[str(text[i]) + str(text[i + 1])] += 1

    # header = ['Bigram', 'Frequency']
    # with open('bi_noover_nospace.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     for items in reversed(sorted(bigramfrequency.items(), key=lambda item: item[1])):
    #         print(items)
    #         writer.writerow(items)

    totaloccurences = sum(bigramfrequency.values())
    percentages = []
    for k, v in dict(reversed(sorted(bigramfrequency.items(), key=lambda item: item[1]))).items():
        pct = round((v / totaloccurences), 5)
        print(k.replace(' ', '_'), str(pct))
        percentages.append(pct)
    print(percentages)
    return percentages


def entropy_calc_h1(probability_list):
    """Function counts the expected h1 value for given probability list
    Prints h1 value in console

    Parameters
    ----------
    probability_list : list
        List of all probabilities for 1-gram

    Returns
    -------
    float
        value of H1
    """
    entropy = 0
    for letter in probability_list:
        if letter != 0:
            entropy += -(letter * math.log(letter, 2))
    print('h1 = ' + str(entropy))
    return entropy


def entropy_calc_h2(probability_list):
    """Function counts the expected h2 value for given probability list
    Prints h2 value in console

    Parameters
    ----------
    probability_list : list
        List of all probabilities for 2-gram

    Returns
    -------
    float
        value of H2
    """
    entropy = 0
    for letter in probability_list:
        if letter != 0:
            entropy += -(letter * math.log(letter, 2))
    entropy = entropy / 2
    print('h2 = ' + str(entropy))


if __name__ == "__main__":
    # cleantextfunc('sourcetext.txt', 'refactoredtext.txt')
    # countletterfrequency(spaces=False)
    # countbigrams(spaces=False, overlapping=False)
    entropy_calc_h2(countbigrams(spaces=True, overlapping=True))
