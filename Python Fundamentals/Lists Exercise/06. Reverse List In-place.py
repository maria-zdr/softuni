list_numbers = list(map(int, input().split(' ')))

for item in range(0, len(list_numbers) // 2):
    tmp = list_numbers[item]
    list_numbers[item] = list_numbers[len(list_numbers) - 1 - item]
    list_numbers[len(list_numbers) - 1 - item] = tmp

print(' '.join(map(str,list_numbers)))