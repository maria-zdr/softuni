import re

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
data = input()
matches = re.findall(pattern, data)

for item in matches:
    print(item, end=' ')