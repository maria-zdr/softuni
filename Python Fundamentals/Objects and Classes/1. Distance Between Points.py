import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(point1, point2):
    result = math.sqrt(pow((point2.x - point1.x), 2) + pow((point2.y - point1.y), 2))
    return result


first_point_data = list(map(float, input().split()))
second_point_data = list(map(float, input().split()))

first_point = Point(first_point_data[0], first_point_data[1])
second_point = Point(second_point_data[0], second_point_data[1])

distance = calc_distance(first_point, second_point)
print(format(distance, '.3f'))
