import cmath


def solve(a, b, c):
    d = b * b - 4 * a * c
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    return x1, x2

if __name__ == "__main__":
    print(solve(1, -3, 2))
