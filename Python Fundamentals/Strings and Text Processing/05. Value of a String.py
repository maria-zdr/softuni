string = input()
case = input()

sum = 0

for ch in string:
    if case == 'UPPERCASE' and 'A' <= ch <= 'Z':
        sum += ord(ch)
    if case == 'LOWERCASE' and 'a' <= ch <= 'z':
        sum += ord(ch)

print('The total sum is: {}'.format(sum))