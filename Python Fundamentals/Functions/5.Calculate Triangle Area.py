def get_triangle_area(base, height):
    return (base * height) / 2


b = float(input())
h = float(input())
print(format(get_triangle_area(b, h), '.12g'))