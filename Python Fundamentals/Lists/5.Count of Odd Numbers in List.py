list_numbers = list(map(int, input().split(' ')))
count = 0

for i in list_numbers:
    if i % 2 != 0:
        count += 1

# count = len(list(filter(lambda num: num % 2 != 0, list_numbers)))

print(count)
