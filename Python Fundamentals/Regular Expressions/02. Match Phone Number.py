import re

pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'
data = input()
matches = re.finditer(pattern, data)

for item in matches:
    print(item.group(), end=' ')