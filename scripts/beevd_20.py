"""Z-score standardisation."""
import statistics
def z_scores(xs):
    mu = statistics.mean(xs)
    sigma = statistics.stdev(xs)
    return [round((x - mu) / sigma, 4) for x in xs]
if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    print(z_scores(data))
