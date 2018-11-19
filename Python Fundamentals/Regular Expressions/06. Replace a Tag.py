import re

pattern = r'<a href=(.*)>(.*)</a>'
replace = r'[URL href=\1]\2[/URL]'

while True:
    data = input()
    if data == 'end':
        break

    data = re.sub(pattern, replace, data)
    print(data)
