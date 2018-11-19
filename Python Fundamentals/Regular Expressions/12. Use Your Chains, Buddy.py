import re

pattern = r'(?<=<p>).*?(?=<\/p>)'
data = input()
matches = re.finditer(pattern, data)
result = ''

for item in matches:
    string = re.sub(' +', ' ', re.sub('[^a-z0-9]', ' ', item.group()))
    for ch in string:
        if 'a' <= ch <= 'm':
            result = result + chr(ord(ch) + 13)
        elif 'n' <= ch <= 'z':
            result = result + chr(ord(ch) - 13)
        else:
            result = result + ch

print(result)
