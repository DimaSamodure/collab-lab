"""Mean, median and mode."""
from statistics import mean, median, mode
def stats(xs):
    return mean(xs), median(xs), mode(xs)
if __name__ == "__main__":
    data = [1, 2, 2, 3, 4]
    print(stats(data))
