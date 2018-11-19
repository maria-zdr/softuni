list_numbers = list(map(float, input().split(' ')))
list_result = []
i = 0

while i < len(list_numbers) - 1:
    tmp = list_numbers[i]
    if list_numbers[i] == list_numbers[i + 1]:
        list_numbers.remove(list_numbers[i])
        list_numbers.remove(list_numbers[i])
        list_numbers.insert(i, tmp + tmp)
        i = 0
    else:
        i += 1

formatted_list = [format(item, '.2g') for item in list_numbers]
print(' '.join(map(str, formatted_list)))
