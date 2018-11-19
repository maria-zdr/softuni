import math

list_numbers = list(map(int, input().split(' ')))
list_result = []

'''
for i in list_numbers:
    if i > 0 and math.sqrt(i) == int(math.sqrt(i)):
        list_result.append(i)
'''

list_result = list(filter(lambda num: num > 0 and math.sqrt(num) == int(math.sqrt(num)), list_numbers))
list_result.sort(reverse= True)

print(' '.join(map(str, list_result)))
