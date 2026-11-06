"""Pearson correlation coefficient."""
import statistics
def correlation(xs, ys):
    return statistics.correlation(xs, ys)
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    print(round(correlation(x, y), 4))
