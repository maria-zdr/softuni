import re

class GitCommit:
    def __init__(self, user, repo, hash, message, additions, deletions):
        self.user = user
        self.repo = repo
        self.hash = hash
        self.message = message
        self.additions = additions
        self.deletions = deletions


pattern = r'https://github.com/([A-Za-z0-9\-]+)/([A-Za-z\-_]+)/commit/((?:\d|[a-f]){40}),(.+?),(\d+),(\d+)'
list_data = []
list_users = []
list_keys = []

while True:
    data = input()
    if data == 'git push':
        break

    if re.match(pattern, data):
        matches = re.finditer(pattern, data)

        for item in matches:
            user = item.group(1)
            repo = item.group(2)
            hash = item.group(3)
            message = item.group(4)
            additions = item.group(5)
            deletions = item.group(6)

            cmt = GitCommit(user, repo, hash, message, additions, deletions)
            list_data.append(cmt)

            if user not in list_users:
                list_users.append(user)
            if (user,repo) not in list_keys:
                list_keys.append((user,repo))

list_users.sort()
list_keys.sort(key=lambda tup: (tup[0],tup[1]))

for u in list_users:
    print('{}:'.format(u))

    list_repos = list(filter(lambda r: r[0] == u,  list_keys))

    for r in list_repos:
        print('  {}:'.format(r[1]))
        add_count = 0
        del_count = 0

        list_commits = list(filter(lambda c: c.user == u and c.repo == r[1], list_data))
        for item in range(len(list_commits)):
            add_count += int(list_commits[item].additions)
            del_count += int(list_commits[item].deletions)
            print('    commit {}: {} ({} additions, {} deletions)'.format(list_commits[item].hash,
                                                                          list_commits[item].message,
                                                                          list_commits[item].additions,
                                                                          list_commits[item].deletions))
            if item == len(list_commits) - 1:
                print('    Total: {} additions, {} deletions'.format(add_count, del_count))
