"""Chi-square goodness-of-fit statistic."""
def chi_square(observed, expected):
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))
if __name__ == "__main__":
    obs = [16, 18, 16, 14, 12, 12]
    exp = [16, 16, 16, 16, 16, 16]
    print(round(chi_square(obs, exp), 4))
