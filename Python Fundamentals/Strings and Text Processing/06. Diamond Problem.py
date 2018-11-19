import re

data = input()
pattern = r'(<[^>]*>)'
matches = re.findall(pattern, data)

if matches:
    for item in matches:
        sum = 0
        for ch in item:
            if ch.isdigit():
                sum += int(ch)
        print('Found {} carat diamond'.format(sum))
else:
    print('Better luck next time')