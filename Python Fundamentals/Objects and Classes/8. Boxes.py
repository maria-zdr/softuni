class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_right = upper_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    @property
    def width(self):
        result = (pow((self.upper_left.x - self.upper_right.x), 2) + pow((self.upper_left.y - self.upper_right.y), 2)) ** 0.5
        return int(result)

    @property
    def height(self):
        result = (pow((self.upper_left.x - self.bottom_left.x), 2) + pow((self.upper_left.y - self.bottom_left.y),2)) ** 0.5
        return int(result)

    def calc_perimeter(self):
        return int(2 * self.width + 2 * self.height)

    def calc_area(self):
        return int(self.width * self.height)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


while True:
    data = input()
    if data == 'end':
        break

    list_data = data.split(' | ')

    upper_left = Point(int(list_data[0].split(':')[0]), int(list_data[0].split(':')[1]))
    upper_right = Point(int(list_data[1].split(':')[0]), int(list_data[1].split(':')[1]))
    bottom_left = Point(int(list_data[2].split(':')[0]), int(list_data[2].split(':')[1]))
    bottom_right = Point(int(list_data[3].split(':')[0]), int(list_data[3].split(':')[1]))

    box = Box(upper_left, upper_right, bottom_left, bottom_right)
    print('Box: {}, {}'.format(box.width, box.height))
    print('Perimeter: {}'.format(box.calc_perimeter()))
    print('Area: {}'.format(box.calc_area()))
