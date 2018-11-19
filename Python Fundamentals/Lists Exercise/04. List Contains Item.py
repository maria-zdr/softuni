list_numbers = list(map(int, input().split(' ')))
n = int(input())
isFound = False

for item in list_numbers:
    if item == n:
        isFound = True

if isFound:
    print('yes')
else:
    print('no')