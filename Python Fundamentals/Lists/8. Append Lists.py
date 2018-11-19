data = input().split('|')
data.reverse()
list_result = []

for item in data:
    list_result.extend(item.split())

print(' '.join(list_result))
