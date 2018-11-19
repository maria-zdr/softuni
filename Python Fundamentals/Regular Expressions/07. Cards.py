import re

pattern = r'10[SHDC]|[2-9AJKQ][SHDC]'
data = input()

matches = matches = re.finditer(pattern, data)

for item in matches:
    print(item.group(), end=' ')
