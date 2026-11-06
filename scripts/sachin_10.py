def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def fib_number(n):
    return fibonacci(n + 1)[n]

if __name__ == "__main__":
    print(fibonacci(10))
    print(fib_number(10))
