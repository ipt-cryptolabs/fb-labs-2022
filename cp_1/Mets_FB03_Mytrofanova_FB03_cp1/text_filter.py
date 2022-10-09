import re

symbols = 'абвгдежзийклмнопрстуфхцчшщыьэюя '

with open('text.txt', 'r', encoding='utf-8') as first_text:
    text = first_text.read()

text = text.lower().replace('ё', 'е').replace('ъ', 'ь').replace('\n', ' ')

filtered_text = text.translate({ord(c): " " for c in "abcdefghijklmnopqrstu….vwxyz«»0123456789!@\"#$%^&*()[]{};:,.—/<>?\|`~–-=_+'"})

filtered_text = " ".join(filtered_text.split())

with open('filtered_text.txt', 'w', encoding='utf-8') as final_text:
    final_text.write(filtered_text)
