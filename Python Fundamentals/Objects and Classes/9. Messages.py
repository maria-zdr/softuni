class User:
    def __init__(self, username):
        self.username = username
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)


class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content


list_users = []
list_messages = []

while True:
    data = input()
    if data == 'exit':
        break

    list_data = data.split()
    if list_data[0] == 'register':
        user = User(list_data[1])
        list_users.append(user)
    else:
        sender = list_data[0]
        receiver = list_data[2]
        content = list_data[3]
        participants = list(filter(lambda u: sender == u.username or receiver == u.username, list_users))

        if len(participants) == 2:
            msg = Message(sender, receiver, content)
            list_messages.append(msg)

            for item in participants:
                if item.username == receiver:
                    item.add_message(msg)

usernames = input().split()
user1 = usernames[0]
user2 = usernames[1]

user1_msgs = []
user2_msgs = []

for item in list_messages:
    if item.sender == user1 and item.receiver == user2:
        user1_msgs.append(item.content)
    elif item.receiver == user1 and item.sender == user2:
        user2_msgs.append(item.content)

if len(user1_msgs) == 0 and len(user2_msgs) == 0:
    print('No messages')
else:
    intersect = min(len(user1_msgs), len(user2_msgs))

    for item in range(0, intersect):
        print('{}: {}'.format(user1, user1_msgs[item]))
        print('{} :{}'.format(user2_msgs[item], user2))

    if len(user1_msgs) > intersect:
        for item in range(intersect, len(user1_msgs)):
            print('{}: {}'.format(user1, user1_msgs[item]))
    elif len(user2_msgs) > intersect:
        for item in range(intersect, len(user2_msgs)):
            print('{} :{}'.format(user2_msgs[item], user2))
