list_numbers = list(map(int, input().split(' ')))

for i in range(0, len(list_numbers)):
    if i % 2 != 0 and list_numbers[i] % 2 != 0:
        print('Index {} -> {}'.format(i, list_numbers[i]))
