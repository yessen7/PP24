import re

txt = str(input())
x = re.search('ab{2,3}', txt)

if x:
    print("yes")
else:
    print("no")
