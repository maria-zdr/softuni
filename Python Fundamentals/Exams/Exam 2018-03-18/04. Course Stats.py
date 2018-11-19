tech_dict = {}
tech_list = []

while True:
    data = input()
    if data == 'end':
        break

    technology = data.split(' - ')[0]
    course_info = data.split(' - ')[1].split(', ')

    if technology not in tech_dict:
        tech_dict[technology] = {}

    for c in course_info:
        course_name = c.split(':')[0]
        participants = int(c.split(':')[1])

        if course_name not in tech_dict[technology]:
            tech_dict[technology][course_name] = participants
        else:
            tech_dict[technology][course_name] += participants

for k, v in tech_dict.items():
    tech_list.append((k, sum(v.values())))

tech_list.sort(key=lambda tup: -tup[1])

print('Most popular: {} ({} participants)'.format(tech_list[0][0], tech_list[0][1]))
print('Least popular: {} ({} participants)'.format(tech_list[-1][0], tech_list[-1][1]))

for t in tech_list:
    print('{} ({} participants):'.format(t[0], t[1]))
    sorted_by_value = sorted(tech_dict[t[0]].items(), key=lambda kv: -kv[1])
    for j in sorted_by_value:
        print('--{} -> {}'.format(j[0], j[1]))

