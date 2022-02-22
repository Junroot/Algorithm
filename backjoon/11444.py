n = int(input())

fibonacci_matrix = [[1, 1], [1, 0]]
result_matrix = [[1, 0], [0, 1]]


def multiply(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] = (result[i][j] + matrix1[i][k] * matrix2[k][j]) % 1000000007
    return result


while n > 0:
    if n % 2 == 1:
        result_matrix = multiply(result_matrix, fibonacci_matrix)
    fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
    n //= 2

print(result_matrix[0][1])

# print(int((5 ** (-0.5)) * ((((1 + 5 ** 0.5) / 2) ** n) - (((1 - 5 ** 0.5) / 2) ** n))) % 1000000007)
