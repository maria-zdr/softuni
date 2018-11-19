key_input = input()
value_input = input()
n = int(input())
dict_data = {}

for i in range(0, n):
    list_data = input().split(' => ')
    list_items = list_data[1].split(';')

    if list_data[0] not in dict_data:
        dict_data[list_data[0]] = []

    for index in range(0, len(list_items)):
        if list_items[index] not in dict_data:
            dict_data[list_data[0]].append(list_items[index])

for item in dict_data:
    result_str = ''
    if key_input in item:
        for val in dict_data[item]:
            if value_input in val:
                result_str += '-{}\n'.format(val)
    if key_input in item:#result_str:
        print('{}:\n{}'.format(item, result_str), end='')
