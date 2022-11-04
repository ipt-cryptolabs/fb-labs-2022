from collections import Counter as c
import re
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
file1 = open("var3.txt", "r", encoding='utf-8')
var3 = file1.read()
var3 = var3.lower()
var3 = re.sub("[^А-аЯ-я]", "", var3)
#punctuations = [".", ",", "!", "?", ";", ":", "-", "1", "2", "3", "4","5", "6", "7","8","9", "0","—","»","«", " ", "’","/n"]
#for k in range(len(punctuations)):
    #var3 = var3.replace(punctuations[k], "")


def encode_function(text, key):
    key_length = len(key)
    encoded_text = []
    for i in range(len(text)):
        y = (alphabet.index(text[i]) + alphabet.index(key[i % key_length])) % 32
        if y == 6:
            y = 'е'
        else:
            y = chr(y + 1072)
        encoded_text.append(y)
    return ''.join(encoded_text)


def conformity_index(text):
    n = len(text)
    index = 0
    text = c(text)
    for i in text:
        index += text[i]*(text[i]-1)
    index = index/(n*(n-1))
    return index

def nearest(lst, target):
  return min(lst, key = lambda x: abs(x-target))

def compare_indexes(text):
    i_list = []
    our_i = conformity_index(var3)
    i1 = conformity_index(encode_function(text, key1))
    i2 = conformity_index(encode_function(text, key2))
    i3 = conformity_index(encode_function(text, key3))
    i4 = conformity_index(encode_function(text, key4))
    i14 = conformity_index(encode_function(text, key5))
    print(i1,i2,i3,i4,i14, our_i)

def find_key(text):
    y = []
    for word_length in range(2,32):
        index_sum = 0
        for i in range(word_length):
            a = []
            for j in range(i, len(text), word_length):
                a.append(text[j])

            print(conformity_index(''.join(a)))
            index_sum += conformity_index(''.join(a))
            print(a)
        y.append(index_sum/word_length)
        print()
    nearest_val = nearest(y, 0.055)
    print(y.index(nearest_val)+2)

    print(y)
find_key(var3)

def key_value(text, key_length, most_popular):
    a = []
    k = []
    z = ''
    for i in range(0,key_length):
        z = ''
        for j in range(i, len(text), key_length):
            z +=text[j]
        a.append(z)
    print('asdas')
    print(a)
    for l in range(key_length):
        #print(list(dict(c(a[l]).most_common(1)).keys())[0])
        most_popular_fragment = list(dict(c(a[l]).most_common(1)).keys())[0]
        x = (alphabet.index(most_popular_fragment) - alphabet.index(most_popular) ) % 32
        x = chr(x + 1072)
        k.append(x)
    print(k)
    return k

keyf = ''.join(key_value(var3, 14, 'о'))


def decrypt_function(text, key):
    decoded_text = []
    for i in range(len(text)):

        y = (alphabet.index(text[i]) - alphabet.index(key[i % 14]) + 32) % 32
        y = chr(y+1072)
        decoded_text.append(y)
    return ''.join(decoded_text)

print(decrypt_function(var3,keyf))

file = open("C:/Users/user/Desktop/text.txt", "r", encoding='utf-8')
text = file.read()
text = re.sub("[^А-аЯ-я]", "", text)
text = text.lower()

key1 = 'во'
key2 = 'так'
key3 = 'рыба'
key4 = 'робот'
key5 = 'деконтаминация'

#print(encode_function(text, key1))
open('text_2.txt', 'w').write(encode_function(text, key1))
open('text_3.txt', 'w').write(encode_function(text, key2))
open('text_4.txt', 'w').write(encode_function(text, key3))
open('text_5.txt', 'w').write(encode_function(text, key4))
open('text_14.txt', 'w').write(encode_function(text, key5))