gladiators_dict = {}
gladiators_list = []

while True:
    data = input()
    if data == 'Ave Cesar':
        break

    if len(data.split(' -> ')) > 1:
        gladiator = data.split(' -> ')[0]
        technique = data.split(' -> ')[1]
        skill = int(data.split(' -> ')[2])

        if gladiator not in gladiators_dict:
            gladiators_dict[gladiator] = {}

        if technique not in gladiators_dict[gladiator]:
            gladiators_dict[gladiator][technique] = skill
        elif technique in gladiators_dict[gladiator] and gladiators_dict[gladiator].get(technique) < skill:
            gladiators_dict[gladiator][technique] = skill
    else:
        gladiator = data.split(' vs ')[0]
        gladiator2 = data.split(' vs ')[1]

        if gladiator in gladiators_dict and gladiator2 in gladiators_dict and gladiators_dict[gladiator].keys() & gladiators_dict[gladiator2].keys():
            gl_total = sum(gladiators_dict[gladiator].values())
            gl2_total = sum(gladiators_dict[gladiator2].values())

            if gl_total > gl2_total:
                gladiator_del = gladiator2
            elif gl_total < gl2_total:
                gladiator_del = gladiator

            del gladiators_dict[gladiator_del]

for k, v in gladiators_dict.items():
    gladiators_list.append((k, sum(v.values())))

gladiators_list.sort(key=lambda tup: (-tup[1], tup[0]))

for g in gladiators_list:
    print('{}: {} skill'.format(g[0], g[1]))
    sorted_by_value = sorted(gladiators_dict[g[0]].items(), key=lambda kv: -kv[1])
    for j in sorted_by_value:
        print('- {} <!> {}'.format(j[0], j[1]))