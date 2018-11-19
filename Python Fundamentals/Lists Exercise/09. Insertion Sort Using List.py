list_numbers = list(map(int, input().split(' ')))
list_result = [list_numbers.pop(0)]

while list_numbers:
    current = list_numbers.pop(0)
    position = 0

    for i in range(0, len(list_result)):
        if list_result[i] <= current:
            position = i + 1

    list_result.insert(position, current)

print(' '.join(map(str, list_result)))
