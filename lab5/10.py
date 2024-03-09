import re

def camel_to_snake_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    snake_case_content = re.sub(r'([a-zа-я])([A-ZА-Я])', r'\1_\2', content)
    snake_case_content = snake_case_content.lower()

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(snake_case_content)


input_file_path = 'row.txt'
output_file_path = 'row10.txt'

camel_to_snake_file(input_file_path, output_file_path)