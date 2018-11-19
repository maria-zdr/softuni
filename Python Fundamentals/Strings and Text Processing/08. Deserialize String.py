chars_list = []

while True:
    data = input()
    if data == 'end':
        break

    ch = data.split(':')[0]
    indexes = list(map(int,data.split(':')[1].split('/')))

    for i in indexes:
        chars_list.append((ch, i))

chars_list.sort(key=lambda tup: tup[1])
result = [c[0] for c in chars_list]

print(''.join(result))