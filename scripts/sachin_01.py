import math

def gcd_lcm(a, b):
    g = math.gcd(a, b)
    l = abs(a * b) // g if g else 0
    return g, l

if __name__ == "__main__":
    print(gcd_lcm(12, 18))
