import re

def match_strings_starting_with_a_and_ending_with_b(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.findall(r'.*а.*б\b', content)
        return matches

file_path = 'row.txt'
result = match_strings_starting_with_a_and_ending_with_b(file_path)

print("Found matches:", result)
