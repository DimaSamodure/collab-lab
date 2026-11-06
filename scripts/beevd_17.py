"""Percentile by nearest-rank and interpolation."""
import statistics
def percentile(xs, p):
    return statistics.quantiles(xs, n=100)[p - 1] if p < 100 else max(xs)
if __name__ == "__main__":
    data = [15, 20, 35, 40, 50]
    print(percentile(data, 50))
    print(percentile(data, 90))
