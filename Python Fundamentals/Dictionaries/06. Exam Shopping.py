dict_data = {}

while True:
    data = input()
    if data.lower() == 'exam time':
        break

    list_data = data.split(' ')

    if list_data[0].lower() == 'stock':
        if list_data[1] in dict_data:
            dict_data[list_data[1]] += int(list_data[2])
        else:
            dict_data[list_data[1]] = int(list_data[2])

    if list_data[0].lower() == 'buy':
        if list_data[1] in dict_data and dict_data[list_data[1]] > 0:
            dict_data[list_data[1]] -= int(list_data[2])
        elif list_data[1] in dict_data and dict_data[list_data[1]] <= 0:
            print('{} out of stock'.format(list_data[1]))
        else:
            print('{} doesn\'t exist'.format(list_data[1]))

for item in dict_data:
    if dict_data[item] > 0:
        print('{0} -> {1}'.format(item, dict_data[item]))