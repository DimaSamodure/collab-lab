"""Population and sample standard deviation."""
import statistics
def std_dev(xs, sample=True):
    return statistics.stdev(xs) if sample else statistics.pstdev(xs)
if __name__ == "__main__":
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    print(std_dev(data))
    print(std_dev(data, sample=False))
