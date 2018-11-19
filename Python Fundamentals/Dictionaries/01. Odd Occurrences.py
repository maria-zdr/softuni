list_data = input().split(' ')
dict_data = {}
list_result = []

for item in list_data:
    if item.lower() in dict_data:
        dict_data[item.lower()] += 1
    else:
        dict_data[item.lower()] = 1

for item in dict_data:
    if dict_data[item] % 2 != 0:
        list_result.append(item)

print(', '.join(list_result))