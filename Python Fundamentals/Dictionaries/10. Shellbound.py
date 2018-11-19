dict_data = {}

while True:
    data = input()
    if data == 'Aggregate':
        break

    region = data.split()[0]
    shell = int(data.split()[1])

    if region not in dict_data:
        dict_data[region] = [shell]
    elif shell not in dict_data[region]:
        dict_data[region].append(shell)

for item in dict_data:
    result = sum(dict_data[item]) - sum(dict_data[item])//len(dict_data[item])
    print('{0} -> {1} ({2:.0f})'.format(item, ', '.join(map(str,dict_data[item])), result))
