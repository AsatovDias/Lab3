import math

# 1
def degree_to_radian(degree):
    return degree * (math.pi / 180)

# 2
def trapezoid_area(height, base1, base2):
    return 0.5 * height * (base1 + base2)

# 3
def regular_polygon_area(num_sides, side_length):
    return (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))

# 4
def parallelogram_area(base, height):
    return base * height
