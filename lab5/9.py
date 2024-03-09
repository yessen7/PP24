import re

def insert_spaces_before_capitals(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    modified_content = re.sub(r'([a-zа-я])([A-ZА-Я])', r'\1 \2', content)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)


input_file_path = 'row.txt'
output_file_path = 'row9.txt'

insert_spaces_before_capitals(input_file_path, output_file_path)
