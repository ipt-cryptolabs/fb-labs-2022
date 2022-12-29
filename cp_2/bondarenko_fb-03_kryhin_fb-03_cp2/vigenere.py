class Vigenere:
    def __init__(self):
        self.alphabet = {
                        'а': 0,
                        'б': 1,
                        'в': 2,
                        'г': 3,
                        'д': 4,
                        'е': 5,
                        'ж': 6,
                        'з': 7,
                        'и': 8,
                        'й': 9,
                        'к': 10,
                        'л': 11,
                        'м': 12,
                        'н': 13,
                        'о': 14,
                        'п': 15,
                        'р': 16,
                        'с': 17,
                        'т': 18,
                        'у': 19,
                        'ф': 20,
                        'х': 21,
                        'ц': 22,
                        'ч': 23,
                        'ш': 24,
                        'щ': 25,
                        'ъ': 26,
                        'ы': 27,
                        'ь': 28,
                        'э': 29,
                        'ю': 30,
                        'я': 31
                            }
        self.letter_codes = {
                            0: 'а',
                            1: 'б',
                            2: 'в',
                            3: 'г',
                            4: 'д',
                            5: 'е',
                            6: 'ж',
                            7: 'з',
                            8: 'и',
                            9: 'й',
                            10: 'к',
                            11: 'л',
                            12: 'м',
                            13: 'н',
                            14: 'о',
                            15: 'п',
                            16: 'р',
                            17: 'с',
                            18: 'т',
                            19: 'у',
                            20: 'ф',
                            21: 'х',
                            22: 'ц',
                            23: 'ч',
                            24: 'ш',
                            25: 'щ',
                            26: 'ъ',
                            27: 'ы',
                            28: 'ь',
                            29: 'э',
                            30: 'ю',
                            31: 'я'
                            }
        self.alphabet_length = len(self.letter_codes)

    @staticmethod
    def blockify(text: str, block_length: int) -> list:
        block_arr = list()
        for i in range(0, len(text) + 1, block_length):
            block_arr.append(text[i:i + block_length])
        return block_arr

    def encrypt(self, plaintext: str, key: str) -> str:
        ciphertext = ''
        key_length = len(key)

        block_arr = self.blockify(plaintext, key_length)

        for block in block_arr:
            for i in range(len(block)):
                letter_code = (self.alphabet[block[i]] + self.alphabet[key[i]]) % self.alphabet_length
                ciphertext += self.letter_codes[letter_code]

        return ciphertext

    def decrypt(self, ciphertext: str, key: str) -> str:
        plaintext = ''
        key_length = len(key)

        block_arr = self.blockify(ciphertext, key_length)

        for block in block_arr:
            for i in range(len(block)):
                letter_code = (self.alphabet[block[i]] - self.alphabet[key[i]]) % self.alphabet_length
                plaintext += self.letter_codes[letter_code]

        return plaintext


def main():
    cipher = Vigenere()
    print("Reading file...\n")
    with open('filtered_text.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    keys = {
            "key2": "фб",
            "key3": "оса",
            "key4": "жало",
            "key5": "хжздл",
            "key12": "ялюблюкрипту",
            "key16": "молибденванадийз",
            "key18": "суперсекретныйключ"
            }

    for key in keys:
        ciphertext = cipher.encrypt(text, keys[key])
        with open(f"./encrypted/{key}_enc.txt", 'w', encoding='utf-8') as f:
            f.write(ciphertext)
        print(f"Ciphertext is written in ./encrypted/{key}_enc.txt")

    print()

    # Check if decrypt(ciphertext) = plaintext
    for key in keys:
        with open(f"./encrypted/{key}_enc.txt", 'r', encoding='utf-8') as f:
            ciphertext = f.read()
        plaintext = cipher.decrypt(ciphertext, keys[key])
        print(f"{key}: {text == plaintext}")


if __name__ == '__main__':
    main()

    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', '')

    cipher = Vigenere()
    plaintext = cipher.decrypt(text, "последнийдозор")

    with open('decoded_text.txt', 'w', encoding='utf-8') as f:
        f.write(plaintext)
