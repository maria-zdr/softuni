dict_data = {}

while True:
    data = input()
    if data == 'drop the media':
        break

    command = data.split()[0]
    post_name = data.split()[1]

    if command == 'post':
        dict_data[post_name] = {'Likes': 0, 'Dislikes': 0, 'Comments':{}}
    elif command == 'like':
        dict_data[post_name]['Likes'] += 1
    elif command == 'dislike':
        dict_data[post_name]['Dislikes'] += 1
    elif command == 'comment':
        author = data.split()[2]
        comment = data.split()[3:]
        dict_data[post_name]['Comments'][author] = comment

for item in dict_data:
    print('Post: {} | Likes: {} | Dislikes: {}'.format(item, dict_data[item]['Likes'],dict_data[item]['Dislikes']))
    print('Comments:')
    if dict_data[item]['Comments']:
        for c in dict_data[item]['Comments']:
            print('*  {}: {}'.format(c, ' '.join(dict_data[item]['Comments'][c])))
    else:
        print('None')
