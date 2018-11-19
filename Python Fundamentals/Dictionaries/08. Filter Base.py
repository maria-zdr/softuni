dict_age = {}
dict_salary = {}
dict_position = {}

while True:
    data = input()
    if data.lower() == 'filter base':
        break
    list_data = data.split(' -> ')

    try:
        tmp = float(list_data[1])
        if tmp % 1 == 0.0:
            dict_age[list_data[0]] = list_data[1]
        else:
            dict_salary[list_data[0]] = list_data[1]
    except ValueError:
        dict_position[list_data[0]] = list_data[1]


filter_base = input()

if filter_base == 'Age':
    for item in dict_age:
        print('Name: {}'.format(item))
        print('Age: {}'.format(dict_age[item]))
        print('=' * 20)
elif filter_base == 'Salary':
    for item in dict_salary:
        print('Name: {}'.format(item))
        print('Salary: {}'.format(dict_salary[item]))
        print('=' * 20)
elif filter_base == 'Position':
    for item in dict_position:
        print('Name: {}'.format(item))
        print('Position: {}'.format(dict_position[item]))
        print('=' * 20)
