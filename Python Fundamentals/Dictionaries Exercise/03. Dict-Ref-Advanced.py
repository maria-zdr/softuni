def isinteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


dict_data = {}

while True:
    data = input()
    if data.lower() == 'end':
        break

    key_data = data.split(' -> ')[0]
    val_data = data.split(' -> ')[1].split(', ')

    if isinteger(val_data[0]):
        if key_data not in dict_data:
            dict_data[key_data] = []
            for item in val_data:
                if isinteger(item):
                    dict_data[key_data].append(item)
        else:
            for item in val_data:
                if item not in dict_data[key_data]:
                    dict_data[key_data].append(item)
    else:
        if val_data[0] in dict_data:
            #dict_data[key_data] = dict_data[val_data[0]]
            dict_data[key_data].extend(dict_data[val_data[0]])

for item in dict_data:
    formatted_list = [format(i, '.2g') for i in dict_data[item]]
    print('{0} === {1}'.format(item, ', '.join(formatted_list)))
