import re

def match_strings_with_a_and_bs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            match = re.search(r'а(б*)', line)
            if match:
                print(f"Line {line_number}: {line.strip()} contains 'а' followed by {match.group(1)} 'б's")
file_path = 'row.txt'
match_strings_with_a_and_bs(file_path)
