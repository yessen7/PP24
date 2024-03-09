import re

def find_sequences_with_underscore_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(r'\b[a-z]+_[a-z]+\b', content)
        return matches

file_path = 'row.txt'
result = find_sequences_with_underscore_in_file(file_path)

print("Found sequences:", result)