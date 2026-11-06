import math

def circle_area(radius):
    return math.pi * radius ** 2

def rect_area(length, width):
    return length * width

if __name__ == "__main__":
    print(f"Circle: {circle_area(5):.2f}")
    print(f"Rectangle: {rect_area(4, 6)}")
