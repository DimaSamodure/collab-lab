def is_perfect(n):
    return n > 1 and sum(d for d in range(1, n) if n % d == 0) == n

if __name__ == "__main__":
    for n in [6, 28, 12]:
        print(n, is_perfect(n))
