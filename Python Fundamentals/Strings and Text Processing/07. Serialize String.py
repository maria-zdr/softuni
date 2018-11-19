string = input()
chars_dict = {}

for i in range(0, len(string)):
    if string[i] not in chars_dict:
        chars_dict[string[i]] = [str(i)]
    else:
        chars_dict[string[i]].append(str(i))

for ch in chars_dict:
    print('{}:{}'.format(ch, '/'.join(chars_dict[ch])))