list_numbers = list(map(int, input().split(' ')))
list_numbers.sort()
count = 1

if len(list_numbers) == 1:
    print('{} -> {}'.format(list_numbers[0], count))
elif len(list_numbers) > 1:
    for item in range(0, len(list_numbers) - 1):
        if list_numbers[item] == list_numbers[item + 1]:
            count += 1
        else:
            print('{} -> {}'.format(list_numbers[item], count))
            count = 1

    # just print the last item, the counter is correct
    print('{} -> {}'.format(list_numbers[len(list_numbers) - 1], count))
