dict_data = {}

while True:
    data = input()
    if data == 'filter':
        break

    topic = data.split(' -> ')[0]
    tags = data.split(' -> ')[1].split(', ')

    if topic not in dict_data:
        dict_data[topic] = tags

    for item in tags:
        if item not in dict_data[topic]:
            dict_data[topic].append(item)

search_words = input().split(', ')

for item in dict_data:
    if set(search_words).issubset(dict_data[item]):
        f_tags = ["#" + i for i in dict_data[item]]
        print('{} | {}'.format(item, ', '.join(f_tags)))