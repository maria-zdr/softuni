list_numbers = list(map(int, input().split(' ')))
isSwapped = False

while True:
    isSwapped = False

    for i in range(1, len(list_numbers)):
        if list_numbers[i - 1] > list_numbers[i]:
            tmp = list_numbers[i]
            list_numbers[i] = list_numbers[i - 1]
            list_numbers[i - 1] = tmp
            isSwapped = True

    if isSwapped == False:
        break

print(' '.join(map(str,list_numbers)))
