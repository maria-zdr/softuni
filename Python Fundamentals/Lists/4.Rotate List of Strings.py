list_values = input().split(' ')

value = list_values.pop()
list_values.insert(0, value)

print(' '.join(list_values))
