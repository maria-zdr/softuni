def pyramid_depth(char, data_list):
    depth = 1
    count = 3

    for item in range (0, len(data_list)):
        if data_list[item].find(char * count) != -1:
            depth += 1
            count += 2
        else:
            break
    return int(depth)


n = int(input())
data = []
pyramids = []

for i in range(0, n):
    data.append(input())

for i in range(0, n - 1):
    chars = set(data[i])
    for ch in chars:
        d = pyramid_depth(ch, data[i+1:])
        if d != 1:
            pyramids.append((ch, d))

pyramids.sort(key=lambda tup: -tup[1])

for i in range(0, pyramids[0][1]):
    print(str(pyramids[0][0]) * (2*i + 1))