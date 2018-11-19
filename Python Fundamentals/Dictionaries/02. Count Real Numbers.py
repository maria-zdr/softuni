list_numbers = list(map(float, input().split()))
list_numbers.sort()
dict_data = {}

for item in list_numbers:
    if item in dict_data:
        dict_data[item] += 1
    else:
        dict_data[item] = 1

for item in dict_data:
    print('{0} -> {1} times'.format(item, dict_data[item]))
