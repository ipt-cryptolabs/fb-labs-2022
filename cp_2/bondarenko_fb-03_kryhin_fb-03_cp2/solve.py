from pprint import pprint


def blockify(text, key_length):
    blocks = list()
    text_length = len(text)
    for i in range(key_length):
        n = i
        res = ""
        while n < text_length:
            res += text[n]
            n += key_length
        blocks.append(res)
    return blocks


def compliance_index(text: str) -> float:
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    comp_index = 0

    for i in alphabet:
        quantity = text.count(i)
        comp_index += quantity * (quantity - 1)

    return (1 / (len(text) * (len(text) - 1))) * comp_index


def main():
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read().replace("\n", '')
    indexes = dict()
    for i in range(2, 31):
        blocks = blockify(text, i)
        avg_index = 0
        for j in blocks:
            avg_index += compliance_index(j)
        avg_index = avg_index / len(blocks)
        indexes[i] = avg_index
    pprint(indexes)
    with open('filtered_text.txt', 'r', encoding='utf-8') as f:
        text = f.read().replace('\n', '')
    print(f"Theoretical value of index: {0.055}")


if __name__ == "__main__":
    main()
