import math


def deg_to_rad(deg):
    return (math.pi/180) * deg


print("Output radian:", deg_to_rad(15))


def trapezoid_area(h, a, b):
    return ((a+b)/2) * h


print("Area of Trapezoid:", trapezoid_area(5, 5, 6))


def polygon_area(n, l): # A = (n/2) * L * R
    area = (n * l**2) / (4 * math.tan(math.pi / n))
    return int(area)


print("Area of Pollygon:", polygon_area(4, 25))


def parallel_area(a, b):
    return a*b


print("Area of parallelogram:", parallel_area(5,6))
