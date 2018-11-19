import re

pattern = r'\b(?:0x)?[0-9A-F]+\b'
#pattern = r'\b(0x)*[0-9A-F]+\b'

data = input()
matches = re.findall(pattern, data)

print(' '.join(matches))
