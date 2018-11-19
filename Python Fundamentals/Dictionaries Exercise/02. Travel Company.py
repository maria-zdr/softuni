dict_data = {}

while True:
    data = input()
    if data.lower() == 'ready':
        break

    list_data = data.split(':')
    list_items = list_data[1].split(',')

    if list_data[0] not in dict_data:
        dict_data[list_data[0]] = {}

    for item in list_items:
        tmp_list = item.split('-')
        dict_data[list_data[0]][tmp_list[0]] = int(tmp_list[1])

while True:
    data = input()
    if data.lower() == 'travel time!':
        break

    list_data = data.split()
