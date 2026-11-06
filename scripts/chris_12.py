def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


for num in range(1, 1000):
    if is_armstrong(num):
        print(num, "is an Armstrong number")
