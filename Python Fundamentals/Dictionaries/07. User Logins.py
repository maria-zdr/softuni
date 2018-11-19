dict_data = {}
failed_logs = 0

while True:
    data = input()
    if data.lower() == 'login':
        break
    list_data = data.split(' -> ')
    dict_data[list_data[0]] = list_data[1]

while True:
    data = input()
    if data.lower() == 'end':
        break
    list_data = data.split(' -> ')

    if list_data[0] in dict_data and dict_data[list_data[0]] == list_data[1]:
        print('{}: logged in successfully'.format(list_data[0]))
    else:
        print('{}: login failed'.format(list_data[0]))
        failed_logs += 1

print('unsuccessful login attempts: {}'.format(failed_logs))
