list_numbers = list(map(int, input().split(' ')))
p = int(input())

# result = list(map(lambda num: num * p, list_numbers))

for i in range(0, len(list_numbers)):
    list_numbers[i] = list_numbers[i] * p

print(' '.join(map(str, list_numbers)))
