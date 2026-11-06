RATES = {"USD": 1.0, "EUR": 0.92, "GBP": 0.79, "JPY": 149.0}

def convert(amount, from_cur, to_cur):
    usd = amount / RATES[from_cur]
    return usd * RATES[to_cur]

if __name__ == "__main__":
    print(f"100 USD = {convert(100, "USD", "EUR"):.2f} EUR")
    print(f"50 EUR = {convert(50, "EUR", "GBP"):.2f} GBP")
