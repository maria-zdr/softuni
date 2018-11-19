string = input()

while True:
    data = input()
    if data == 'end':
        break

    command = data.split()[0]
    if command == 'Left':
        offset = int(data.split()[1]) % len(string)
        string = string[offset:] + string[:offset]
    elif command == 'Right':
        offset = int(data.split()[1]) % len(string)
        string = string[-offset:] + string[:-offset]
    elif command == 'Insert':
        i = int(data.split()[1])
        string = string[:i] + data.split()[2] + string[i:]
    elif command == 'Delete':
        start = int(data.split()[1])
        end = int(data.split()[2]) + 1
        string = string[:start] + string[end:]

print(string)