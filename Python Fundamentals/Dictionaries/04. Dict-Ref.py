dict_data = {}

while True:
    data = input().split(' = ')
    if data[0] == 'end':
        break

    if data[1].isdigit():
        dict_data[data[0]] = int(data[1])
    elif data[1] in dict_data:
        dict_data[data[0]] = dict_data.get(data[1])

for item in dict_data:
    print('{0} === {1}'.format(item, dict_data[item]))
