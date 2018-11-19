import re

search = input()
result = []
sentence_pattern = r'^[A-Z].*[.!?]$'

while True:
    data = input()
    if data == 'end':
        break

    if re.match(sentence_pattern, data):
        words = re.findall(r'\w+', data)
        for item in words:
            symbols = re.findall(search[0], item)
            if len(symbols) >= int(search[1]):
                result.append(item)

print(', '.join(result))