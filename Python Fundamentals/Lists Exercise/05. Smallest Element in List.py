list_numbers = list(map(int, input().split(' ')))
smallest = list_numbers[0]

for item in list_numbers:
    if item < smallest:
        smallest = item

print(smallest)
