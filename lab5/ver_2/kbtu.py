import re

txt = str(input())

kbtu = r"[a-z]_[a-z]+@kbtu\.kz"

x = re.match(kbtu, txt)

if x:
    print("yes")
else:
    print("no")
