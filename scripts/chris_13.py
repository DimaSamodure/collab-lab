def bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def category(value):
    if value < 18.5:
        return "Underweight"
    if value < 25:
        return "Normal weight"
    if value < 30:
        return "Overweight"
    return "Obese"

if __name__ == "__main__":
    result = bmi(70, 1.75)
    print(f"BMI: {result:.1f} ({category(result)})")
