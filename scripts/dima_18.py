def poly_eval(coeffs, x):
    result = 0
    for c in coeffs:
        result = result * x + c
    return result

if __name__ == "__main__":
    print(poly_eval([2, -3, 1], 4))
