import re

txt = str(input())
x = re.search("ab*", txt)

if x:
    print("yes")
else:
    print("no")
