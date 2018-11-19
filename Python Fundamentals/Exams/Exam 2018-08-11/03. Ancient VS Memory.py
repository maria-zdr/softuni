input_string = []

while True:
    data = input()
    if data == 'DEBUG':
        break
    input_string.extend(list(map(int, data.split())))

for i in range(len(input_string)):
    if input_string[i] == 32656 and len(input_string[i:]) > 6:
        cnt = input_string[i + 4]
        if input_string[i + 1] == 19759 and input_string[i + 2] == 32763 and input_string[i + 3] == 0 and input_string[i + 5] == 0 and len(input_string[i + 4:]) >= cnt:
            for j in range(i + 5, i + 6 + cnt):
                print(chr(input_string[j]), end='')
            print()

