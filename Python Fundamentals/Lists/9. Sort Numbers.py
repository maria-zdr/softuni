list_numbers = list(map(int, input().split(' ')))
list_numbers.sort()
print(' <= '.join(map(str, list_numbers)))