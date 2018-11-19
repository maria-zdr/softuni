import re

pattern = r"(?P<tail>>*)<(?P<body>\(+)(?P<status>[-'x])>"
data = input()
matches = re.finditer(pattern, data)
count = 0

for item in matches:
    count += 1

    tail = item.group('tail')
    body = item.group('body')
    status = item.group('status')

    if len(tail) > 5:
        tail_type = 'Long'
    elif len(tail) > 1:
        tail_type = 'Medium'
    elif len(tail) == 1:
        tail_type = 'Short'
    elif len(tail) == 0:
        tail_type = 'None'

    if len(body) > 10:
        body_type = 'Long'
    elif len(body) > 5:
        body_type = 'Medium'
    else:
        body_type = 'Short'

    if status == "'":
        st_txt = 'Awake'
    elif status == "-":
        st_txt = 'Asleep'
    elif status == "x":
        st_txt = 'Dead'
    else:
        st_txt = ''

    print('Fish {}: {}<{}{}>'.format(count, tail, body, status))
    if len(tail) == 0:
        print('  Tail type: {}'.format(tail_type))
    else:
        print('  Tail type: {} ({} cm)'.format(tail_type, len(tail) * 2))
    print('  Body type: {} ({} cm)'.format(body_type, len(body)*2))
    print('  Status: {}'.format(st_txt))

if count == 0:
    print('No fish found.')