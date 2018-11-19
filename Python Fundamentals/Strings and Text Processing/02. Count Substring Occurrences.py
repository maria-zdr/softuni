string = input().lower()
search_string = input().lower()

count = 0
index = 0

while index != -1:
    index = string.find(search_string, index)
    if index != -1:
        index += 1
        count += 1

print(count)
