def matrix_addition(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]#list comprehesive booltai hai isko
    return result

def matrix_transpose(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]#ye bhi list comprehensive
    return result

def matrix_multiplication(matrix1, matrix2):
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]#list comprehensive meaning list k andhar hi loop start karna samjha bangladeshi
    return result

# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Matrix Addition
print("\nAddition of Matrices:")
addition_result = matrix_addition(matrix1, matrix2)
for row in addition_result:
    print(row)

# Matrix Transpose
print("\nTranspose of Matrix 1:")
transpose_result = matrix_transpose(matrix1)
for row in transpose_result:
    print(row)

# Matrix Multiplication
print("\nMultiplication of Matrices:")
multiplication_result = matrix_multiplication(matrix1, matrix2)
for row in multiplication_result:
    print(row)
