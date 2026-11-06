def tip_total(bill, percent=15, people=1):
    tip = bill * percent / 100
    total = bill + tip
    return round(tip, 2), round(total, 2), round(total / people, 2)

if __name__ == "__main__":
    print(tip_total(100, 20, 4))
    print(tip_total(48.50, 15, 2))
