while True:
    state = input()
    if state == 'collapse':
        break

    fiction = input()

    while len(fiction) > 0:
        state = state.replace(fiction, '')
        fiction = fiction[1:-1]

    state = state.strip()
    if state == '':
        print('(void)')
    else:
        print(state)