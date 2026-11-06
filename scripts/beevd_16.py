"""Simple linear regression by least squares."""
import statistics
def linear_regression(xs, ys):
    return statistics.linear_regression(xs, ys)
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
    slope, intercept = linear_regression(x, y)
    print(round(slope, 4), round(intercept, 4))
