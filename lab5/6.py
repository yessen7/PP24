def replace_spaces_commas_dots_with_colon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        modified_content = content.replace(' ', ':').replace(',', ':').replace('.', ':')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)


file_path = 'row.txt'
replace_spaces_commas_dots_with_colon(file_path)
