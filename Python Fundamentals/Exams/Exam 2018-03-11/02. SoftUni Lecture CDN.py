course_list = []
server = 1
server_capacity = 600

while True:
    data = input().split()
    if data[0] == 'scrape':
        break

    info = data[0].split(';')
    tmp_dict = {}
    for i in info:
       key = i.split(':')[0]
       value = i.split(':')[1]
       if key == 'duration':
           h = int(value.split('h')[0])
           m = int(value.split('h')[1][:-1])
           value = h*60 + m

           if server_capacity - value >= 0:
               tmp_dict['server'] = server
               server_capacity -= value
           else:
               server_capacity = 600
               server +=1
               tmp_dict['server'] = server
               server_capacity -= value
       tmp_dict[key] = value


    course_list.append(tmp_dict)

result = [c for c in course_list if c[data[1]] == data[2]]
total_duration = 0
for item in result:
    print('https://streamcdn{}.softuni.bg/course={}&lecture={}&trainer={}'.format(item['server'], item['course'], item['lecture'], item['trainer']))
    total_duration += item['duration']


print('total duration: {0:02d}:{1:02d}:00'.format(total_duration//60, total_duration%60))
