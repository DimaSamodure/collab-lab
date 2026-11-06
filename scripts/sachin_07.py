from datetime import date

def days_between(d1, d2):
    return abs((d2 - d1).days)

def parse(iso):
    y, m, d = map(int, iso.split("-"))
    return date(y, m, d)

if __name__ == "__main__":
    print(days_between(parse("2026-01-01"), parse("2026-11-06")))
