import re

pattern = r'([^&=?]*)=([^&=]*)'
pattern_spaces = r'((%20|\+)+)'

while True:
    data = input()
    if data == 'END':
        break

    matches = re.finditer(pattern, data)
    dict_data = {}

    for item in matches:
        keys = re.sub(pattern_spaces, ' ', item.group(1)).strip()
        values = re.sub(pattern_spaces, ' ', item.group(2)).strip()

        if keys not in dict_data:
            dict_data[keys] = [values]
        else:
            dict_data[keys].append(values)

    for item in dict_data:
        print('{0}=[{1}]'.format(item, ', '.join(dict_data[item])), end='')
    print()