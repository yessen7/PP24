import re

def find_sequences_upper_lower(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(r'\b[A-Za-zА-Яа-я][a-zа-я]+\b', content)
        return matches

file_path = 'row.txt'
result = find_sequences_upper_lower(file_path)

print("Found sequences:", result)