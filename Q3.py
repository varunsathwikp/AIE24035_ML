
def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result

def matrix_power(A, m):
    result = A
    for _ in range(1, m):
        result = multiply_matrices(result, A)
    return result

def main():
    matrix = [[1, 2], [3, 4]]
    print("Matrix Power:", matrix_power(matrix, 2))

main()
