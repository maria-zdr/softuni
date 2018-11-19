dict_data = {}

while True:
    data = input().replace(' ', '').split(':')
    if data[0].lower() == 'over':
        break

    if data[0].isdigit():
        dict_data[data[1]] = data[0]
    else:
        dict_data[data[0]] = data[1]

for item in sorted(dict_data):
    print('{0} -> {1}'.format(item, dict_data[item]))
