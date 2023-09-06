import random


matrix1 = [[random.randint(1,10) for _ in range(3)] for _ in range(3)]


matrix2 = [[random.randint(1,10) for _ in range(3)] for _ in range(3)]


def mult(mat1, mat2):
    result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result_matrix[i][j] += mat1[i][k] * mat2[k][j]
    return result_matrix

result_matrix = mult(matrix1, matrix2)


print("Перша матриця:")
for row in matrix1:
    print(row)

print("\nДруга матриця:")
for row in matrix2:
    print(row)

print("\nРезультат множення матриць:")
for row in result_matrix:
    print(row)