def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

if __name__ == "__main__":
    print(det2([[3, 8], [4, 6]]))
