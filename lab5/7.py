def snake_to_camel_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.split('_')
    camel_case_content = words[0] + ''.join(word.capitalize() for word in words[1:])

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(camel_case_content)


input_file_path = 'row.txt'
output_file_path = 'row7.txt'

snake_to_camel_file(input_file_path, output_file_path)
