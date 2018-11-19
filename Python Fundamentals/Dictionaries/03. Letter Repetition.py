data = input()
dict_data = {}

for item in data:
    if item in dict_data:
        dict_data[item] += 1
    else:
        dict_data[item] = 1

for item in dict_data:
    print('{0} -> {1}'.format(item, dict_data[item]))
