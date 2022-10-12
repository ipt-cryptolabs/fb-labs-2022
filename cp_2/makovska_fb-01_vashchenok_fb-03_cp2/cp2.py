import re

alfavit_d = 'абвгдеёэжзиыйклмнопрстуфхцчшщъьюя'


def filter_txt(file_name):
    file = open(file_name, encoding="utf8")
    t = file.read()
    file.close()
    lowered_text = t.lower()
    new_txt = re.sub(r'[^а-яё]', '',lowered_text)
    new_file = open('filtered.txt', 'w')
    new_file.write(new_txt)
    new_file.close()


def dict_stv():
    dict_d = {}
    num = 0
    for i in alfavit_d:
        dict_d.update({i: num})
        num += 1
    return dict_d


def generkl_d(text, key):
    n = len(text) // len(key)
    k = len(text) % len(key)
    new_key = key * n + key[:k]
    return new_key


def ascii_cod_d(text):
    list_code = []
    d = dict_stv()
    for i in text:
        for value in d:
            if i == value:
                list_code.append(d[value])
    return list_code


def to_text_d(asciicd):
    list_code = []
    d = dict_stv()
    for i in asciicd:
        for value in d:
            if i == d[value]:
                list_code.append(value)
    return list_code


def encrypt_d(text, key):
    text = ascii_cod_d(text)
    key = ascii_cod_d(key)
    res = []
    for t, k in zip(text, key):
        let = (t + k) % 33
        res.append(let)
    return res


filter_txt('ourtext.txt')
file_d = open("filtered_d.txt")
filtered_d = file_d.read()
file_d.close()

key_d = list('аб')
gen_key_d = generkl_d(filtered_d, key_d)
cryptedlist_d = encrypt_d(filtered_d, gen_key_d)
cryptedlist_d = to_text_d(cryptedlist_d)
cryptedtext_d = ''
for i in cryptedlist_d:
    cryptedtext_d += i
#print(cryptedtext_d)
cryptfile_d = open('cryptfile_d.txt', 'w')
cryptfile_d.write(cryptedtext_d)
cryptfile_d.close()




#print


alfavit = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
alfavit_arr = ['а', 'б', 'в', 'г', 'д', 'е', 'ж','з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']
  

def frequency_of_letters(txt, alfavit):
    dictionary = {} # словник зі значеннями літера:кількість зустріваності
    for l in alfavit:
        dictionary[l] = 0
    for l in txt: # якщо літера є в тексті, збільшуємо її частоту зустріваності на 1
        dictionary[l] += 1

    freq = {} # рахуємо частоту для кожної літери і заносимо в словник
    for l in alfavit:
        freq[l] = (dictionary[l])/len(txt)
        freq[l] = round(freq[l], 6)
    return freq

def compliance_index(text, index = 0):
    for bukva in alfavit:
        count = 0
        for i in range(0,len(text)):
            if (text[i] == bukva):
                count+=1
        index = index + count * (count-1)
    index = index / (len(text)*(len(text)-1))
    return index


def divide_into_blocks(text, block_lenght):
    blocks = []
    for n in range(0,block_lenght):
        blocks.append(text[n])
    for k in range(block_lenght,len(text)):
        blocks[k%block_lenght] += text[k]
    return blocks


def get_key(text):
    def find_key(a, b, alfavit):
        result = (alfavit.index(a)-alfavit.index(b))%32
        return result    
    # шукаємо довжину/період ключа за 1 способом
    index = []
    for r in range (2, 32): 
        blocks = divide_into_blocks(text, r)
        ind = []
        for n in blocks:
            ind.append(compliance_index(n)) # для кожного блоку рахуємо індекси відповідності
        index.append(sum(ind)/len(ind)) # середнє значення індексу для кожної довжини блоку
    print(index)

    key_length = []
    for n in index:
        if n > 0.055:  # 0.055 - індекс рос мови
            key_length.append(index.index(n) + 2) # у кого більші, записуємо, бо це вірогідніше за все і буде періодом
    final_key_length = min(key_length) # найближчий до 0.055 - індекса рос мови
    print('Знайдена довжина ключа: ',final_key_length)

# шукаємо сам ключ
    key = []
    max_freq_letter = 'оеаи'
    blocks = divide_into_blocks(text, final_key_length)
    for n in blocks:
        freq_dict = frequency_of_letters(n, alfavit)
        m = max(freq_dict, key=freq_dict.get)
        key.append(alfavit_arr[find_key(m, max_freq_letter[0], alfavit)])
# ключ було вгадано недокінця, проте комп сам не може визначити чи отриманий ключ змістовний, тому інтуїтивно 
# було встановлено, що ключ = *делолисоборотней*. для того, щоб підібрати літери, які були підібрані неправильно
# повторимо процес розшифрування, але з другою найбільш зустріваною літерою
    real_key = ['д','е','л','о','л','и','с','о','б','о','р','о','т','н','е','й']
    for i in range(0,final_key_length):
        if key[i] != real_key[i]:
            freq_dict = frequency_of_letters(blocks[i], alfavit)
            m = max(freq_dict, key=freq_dict.get)
            key[i] = alfavit_arr[find_key(m, max_freq_letter[1], alfavit)]
    key_str = ''
    for i in key:
        key_str += i
    print('Знайдений ключ: ', key_str)
    return key_str




def decryption(key, text, alfavit):
    result = ""
    for n in range(0,len(text)):
        result += alfavit_arr[((ord(text[n]) - ord(key[n % len(key)])) % 32)]
    print("Текст з ключем ", key, "розшифровано")
    file_to_write = open("decrypted.txt", 'w')
    file_to_write.write(result)
    file_to_write.close()


filter_txt('text.txt')
file = open( "filtered.txt")
text = file.read()
file.close()

# отримали ключ *девелииоборойдей*, бачимо що більшість літер вгадані правильно
# але треба трохи підправити ключ
final_key = "делолисоборотней"
key = get_key(text)
decryption(key, text, alfavit)
