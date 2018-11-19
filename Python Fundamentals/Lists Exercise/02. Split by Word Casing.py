list_specials = [',', ';', ':', '.', '!', '(', ')', '\"', '\'', '\\', '/', '[', ']']

list_lower = []
list_mixed = []
list_upper = []

data = input()

for item in list_specials:
    data = data.replace(item, ' ')

list_data = data.split(' ')

for item in list_data:
    if item != '':
        if item == item.upper() and item.isalpha():
            list_upper.append(item)
        elif item == item.lower() and item.isalpha():
            list_lower.append(item)
        else:
            list_mixed.append(item)

print('Lower-case: {}'.format(', '.join(list_lower)))
print('Mixed-case: {}'.format(', '.join(list_mixed)))
print('Upper-case: {}'.format(', '.join(list_upper)))
