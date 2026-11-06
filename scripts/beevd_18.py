"""Text histogram with fixed-width bins."""
def histogram(xs, bins=5):
    lo, hi = min(xs), max(xs)
    width = (hi - lo) / bins or 1
    counts = [0] * bins
    for x in xs:
        counts[min(bins - 1, int((x - lo) / width))] += 1
    return counts
if __name__ == "__main__":
    data = [1, 2, 2, 3, 5, 8, 9, 10]
    print(histogram(data, bins=4))
