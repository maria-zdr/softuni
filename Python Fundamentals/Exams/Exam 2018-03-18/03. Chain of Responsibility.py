import re

n = int(input())
robots = []
pattern = r"(\b[0-9]+[A-Z][a-z]+([0-9A-Z])\2+\b)"
msg = ''

for i in range(0, n):
    line = input()
    matches = re.findall(pattern, line)

    first = matches[0][0]
    last = matches[-1][0]

    if robots:
        if robots[-1] != first:
            msg = 'Broke the chain!'
            break

    if len(robots) == 0:
        robots.append(first)
        robots.append(last)
    elif len(matches)> 1:
        robots.append(last)

    if len(matches) == 1:
        if line[-2:] == '!!':
            msg = 'Found the manager!: {}'.format(matches[0][0])
        else:
            msg = 'Did not find the manager!'
        break


print(msg)
print('Chain: {}'.format('->'.join(robots)))
