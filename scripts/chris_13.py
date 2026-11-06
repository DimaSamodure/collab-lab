import cmath


def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    r1 = (-b + cmath.sqrt(d)) / (2 * a)
    r2 = (-b - cmath.sqrt(d)) / (2 * a)
    return r1, r2


if __name__ == "__main__":
    print(solve_quadratic(1, -3, 2))
    print(solve_quadratic(1, 2, 5))
