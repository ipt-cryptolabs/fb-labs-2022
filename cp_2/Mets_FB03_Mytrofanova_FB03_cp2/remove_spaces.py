with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
no_spaces_text = text.replace(' ', '')

with open('filtered_text.txt', 'w', encoding='utf-8') as final_text:
    final_text.write(no_spaces_text)