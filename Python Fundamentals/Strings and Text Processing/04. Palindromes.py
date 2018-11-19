data = input().split()
result = []

for word in data:
    if list(word) == list(reversed(word)) and word not in result:
        result.append(word)

result.sort(key=str.upper)
print(', '.join(result))
