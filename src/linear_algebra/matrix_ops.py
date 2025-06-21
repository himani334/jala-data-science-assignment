
def matrix_addition(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

def matrix_multiplication(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            cell = 0
            for k in range(len(A[0])):
                cell += A[i][k] * B[k][j]
            row.append(cell)
        result.append(row)
    return result

# Example
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Addition:", matrix_addition(A, B))
print("Multiplication:", matrix_multiplication(A, B))