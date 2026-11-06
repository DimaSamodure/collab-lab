"""Date difference utility."""
from datetime import date


def days_between(start, end):
    return (end - start).days


if __name__ == "__main__":
    print(days_between(date(2026, 1, 1), date(2026, 11, 6)))
