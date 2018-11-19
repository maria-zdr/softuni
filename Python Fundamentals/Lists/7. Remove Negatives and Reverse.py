list_numbers = list(map(int, input().split(' ')))
list_positives = []

'''
for i in list_numbers:
    if i > 0:
        list_positives.append(i)
'''

list_positives = list(filter(lambda num: num > 0, list_numbers))
list_positives.reverse()

if list_positives:
    print(' '.join(map(str, list_positives)))
else:
    print('empty')
