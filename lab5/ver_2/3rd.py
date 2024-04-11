import re

txt = input()
x = re.findall("[^A-Z]\w+_\w+", txt)

if x:
    print("yes")
else:
    print("no")


