def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print(transpose(m))
