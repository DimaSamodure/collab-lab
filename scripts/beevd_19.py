"""Normal distribution pdf and cdf."""
import math
def normal_pdf(x, mu=0.0, sigma=1.0):
    return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))
def normal_cdf(x, mu=0.0, sigma=1.0):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))
if __name__ == "__main__":
    print(round(normal_pdf(0), 4))
    print(round(normal_cdf(0), 4))
