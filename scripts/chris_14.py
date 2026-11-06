def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

if __name__ == "__main__":
    for s in [95, 82, 74, 61, 45]:
        print(s, grade(s))
