n = int(input())
dict_data = {}

for i in range(0, n):
    list_data = input().split(' -> ')
    list_items = list_data[1].split(',')

    if list_data[0] not in dict_data:
        dict_data[list_data[0]] = {}

    for item in list_items:
        if item in dict_data[list_data[0]]:
            dict_data[list_data[0]][item] += 1
        else:
            dict_data[list_data[0]][item] = 1

find_item = input().split(' ')

for item in dict_data:
    print('{} clothes:'.format(item))
    for key in dict_data[item]:
        if item == find_item[0] and key == find_item[1]:
            print('* {} - {} (found!)'.format(key, dict_data[item][key]))
        else:
            print('* {} - {}'.format(key, dict_data[item][key]))
