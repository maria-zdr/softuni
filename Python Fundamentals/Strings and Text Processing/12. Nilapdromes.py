while True:
    string = input()
    if string == 'end':
        break

    for i in range(len(string) // 2 + 1, -1, -1):
        if string[:i] == string[-i:]:
            core = string[i: -i]
            border = string[:i]
            if core != '':
                print(core + border + core)
                break
