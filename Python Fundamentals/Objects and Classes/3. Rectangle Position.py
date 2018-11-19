class Rectangle:
    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.right = left + width
        self.bottom = top + height


def is_inside(r1, r2):
    result = r1.left >= r2.left and r1.right <= r2.right and r1.top <= r2.top and r1.bottom <= r2.bottom
    return result


first_data = list(map(float, input().split()))
first_rectangle = Rectangle(first_data[0], first_data[1], first_data[2], first_data[3])
second_data = list(map(float, input().split()))
second_rectangle = Rectangle(second_data[0], second_data[1], second_data[2], second_data[3])

if is_inside(first_rectangle, second_rectangle):
    print('Inside')
else:
    print('Not inside')