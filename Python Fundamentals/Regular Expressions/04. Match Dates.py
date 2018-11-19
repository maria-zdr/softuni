import re

pattern = r'\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b'

data = input()
matches = re.finditer(pattern, data)

for item in matches:
    day = item.group('day')
    month = item.group('month')
    year = item.group('year')

    print('Day: {}, Month: {}, Year: {}'.format(day, month, year))

