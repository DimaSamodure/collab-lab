"""Simple moving average over a window."""
def moving_average(xs, window=3):
    return [round(sum(xs[i:i + window]) / window, 4) for i in range(len(xs) - window + 1)]
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    print(moving_average(data))
    print(moving_average(data, window=2))
