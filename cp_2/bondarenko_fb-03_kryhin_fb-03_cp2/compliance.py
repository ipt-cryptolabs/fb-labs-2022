from os import listdir


def compliance_index(text: str) -> float:
    alphabet = "абвгдежзийклмнопрстуфхцчшщыьъэюя"
    comp_index = 0

    for i in alphabet:
        quantity = text.count(i)
        comp_index += quantity * (quantity - 1)

    return (1 / (len(text) * (len(text) - 1))) * comp_index


def main():
    for file in listdir("./encrypted"):
        with open(f"./encrypted/{file}", 'r', encoding='utf-8') as f:
            print(f"filename: {file} index = {compliance_index(f.read())}")

    with open('filtered_text.txt', 'r', encoding='utf-8') as f:
        text = f.read().replace("\n", '')

    print(f"\nplaintext (Kafka): {compliance_index(text)}")


if __name__ == '__main__':
    main()
