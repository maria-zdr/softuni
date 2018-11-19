import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(point1, point2):
    result = math.sqrt(pow((point2.x - point1.x), 2) + pow((point2.y - point1.y), 2))
    return result


n = int(input())
list_points = []
closest_points = []

for i in range(0, n):
    data = list(map(float, input().split()))
    list_points.append(Point(data[0], data[1]))

if len(list_points) > 1:
    min_distance = calc_distance(list_points[0], list_points[1])
    closest_points = [list_points[0], list_points[1]]

    for i in range(0, len(list_points)):
        for j in range(i + 1, len(list_points)):
            temp_distance = calc_distance(list_points[i], list_points[j])
            if temp_distance < min_distance:
                closest_points.clear()
                closest_points = [list_points[i], list_points[j]]
                min_distance = temp_distance

    print(format(min_distance, '.3f'))
    for item in closest_points:
        print('({0:.2g}, {1:.2g})'.format(item.x, item.y))
