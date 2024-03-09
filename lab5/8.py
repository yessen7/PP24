import re

def split_at_uppercase_file(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    splits = re.findall(r'[A-Z][^A-Z]*', content)
    return splits


input_file_path = 'row.txt'
result = split_at_uppercase_file(input_file_path)

print("Result:", result)
