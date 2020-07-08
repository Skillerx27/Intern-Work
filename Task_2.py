import re
s = input()
x = re.sub(r'\W+', '', s)
print(x)