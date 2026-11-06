def km_to_miles(km):
    return km * 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

if __name__ == "__main__":
    print(f"10 km = {km_to_miles(10):.2f} miles")
    print(f"5 kg = {kg_to_pounds(5):.2f} lb")
    print(f"20 C = {celsius_to_fahrenheit(20):.1f} F")
