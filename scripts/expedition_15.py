import sys
from collections import Counter
def count_levels(path):
    with open(path) as f:
        levels = [line.split()[2] for line in f if len(line.split()) > 2]
    return dict(Counter(levels))
if __name__ == "__main__":
    print(count_levels(sys.argv[1]))
