"""Tip calculator utility."""


def tip_amount(bill, percent):
    return round(bill * percent / 100, 2)


def total_with_tip(bill, percent):
    return round(bill + tip_amount(bill, percent), 2)


if __name__ == "__main__":
    print(tip_amount(80, 15), total_with_tip(80, 15))
