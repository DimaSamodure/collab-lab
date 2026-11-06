def box_volume(length, width, height):
    return length * width * height

def sphere_volume(radius):
    import math
    return 4 / 3 * math.pi * radius ** 3

if __name__ == "__main__":
    print(f"Box: {box_volume(3, 4, 5)}")
    print(f"Sphere: {sphere_volume(2):.2f}")
