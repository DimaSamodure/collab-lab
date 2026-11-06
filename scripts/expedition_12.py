def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

for n in range(1, 1000):
    if is_armstrong(n):
        print(n)
