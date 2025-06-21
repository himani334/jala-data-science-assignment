import random

a = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]

# Manual sum, mean, std
total = 0
count = 0
for row in a:
    for val in row:
        total += val
        count += 1
mean = total / count

# Calculate variance and std deviation
variance = 0
for row in a:
    for val in row:
        variance += (val - mean) ** 2
std_dev = (variance / count) ** 0.5

print("Matrix:", a)
print("Sum:", total)
print("Mean:", mean)
print("Std Dev:", std_dev)

# 2. Cumulative sum of 1D array
arr1 = list(range(10))
cumsum = []
s = 0
for val in arr1:
    s += val
    cumsum.append(s)
print("Cumulative Sum:", cumsum)

# 3. 2x3 array operations
a1 = [[random.randint(1, 10) for _ in range(3)] for _ in range(2)]
a2 = [[random.randint(1, 10) for _ in range(3)] for _ in range(2)]

add = [[a1[i][j] + a2[i][j] for j in range(3)] for i in range(2)]
sub = [[a1[i][j] - a2[i][j] for j in range(3)] for i in range(2)]
mul = [[a1[i][j] * a2[i][j] for j in range(3)] for i in range(2)]
div = [[a1[i][j] / a2[i][j] for j in range(3)] for i in range(2)]

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)

# 4. 4x4 Identity matrix
identity = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
print("Identity Matrix:", identity)

# 5. Broadcasting division
a = [5, 10, 15, 20, 25]
broadcasted = [x / 5 for x in a]
print("Broadcasted Division:", broadcasted)
# ✅ Array Manipulation

# 6. Reshape 1D array to 3x4
array_1d = list(range(12))
reshaped_3x4 = []
for i in range(0, 12, 4):
    reshaped_3x4.append(array_1d[i:i+4])
print("Reshaped to 3x4:", reshaped_3x4)

# 7. Flatten 3x3 matrix to 1D
matrix_3x3 = [[1,2,3],[4,5,6],[7,8,9]]
flattened = []
for row in matrix_3x3:
    for val in row:
        flattened.append(val)
print("Flattened:", flattened)

# 8. Stack 3x3 matrices
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[9,8,7],[6,5,4],[3,2,1]]

# Horizontal stack
h_stack = []
for i in range(3):
    h_stack.append(m1[i] + m2[i])

# Vertical stack
v_stack = m1 + m2

print("Horizontal Stack:", h_stack)
print("Vertical Stack:", v_stack)

# 9. Concatenate arrays of different sizes along new axis
a1 = [1, 2, 3]
a2 = [4, 5]
max_len = max(len(a1), len(a2))
concatenated = []
for i in range(max_len):
    row = []
    if i < len(a1): row.append(a1[i])
    else: row.append(None)
    if i < len(a2): row.append(a2[i])
    else: row.append(None)
    concatenated.append(row)
print("Concatenated on new axis:", concatenated)

# 10. Transpose 3x2 and reshape to 3x2
original = [[1, 2], [3, 4], [5, 6]]
transposed = [[original[j][i] for j in range(3)] for i in range(2)]
reshaped = []
flat = []
for row in transposed:
    for val in row:
        flat.append(val)
for i in range(0, 6, 2):
    reshaped.append(flat[i:i+2])
print("Transposed:", transposed)
print("Reshaped to 3x2:", reshaped)


# ✅ Indexing and Slicing

# 11. Extract elements 2 to 10 with step 2
array = list(range(15))
sliced = []
for i in range(2, 11, 2):
    sliced.append(array[i])
print("Sliced [2:10:2]:", sliced)

# 12. Extract sub-matrix rows 1 to 3, cols 2 to 4 from 5x5 matrix
matrix_5x5 = [[i + j * 5 for i in range(5)] for j in range(5)]
sub_matrix = []
for i in range(1, 4):
    row = []
    for j in range(2, 5):
        row.append(matrix_5x5[i][j])
    sub_matrix.append(row)
print("Sub-matrix:", sub_matrix)

# 13. Replace all elements >10 with 10
array = [3, 12, 7, 15, 9, 20, 6]
replaced = []
for val in array:
    if val > 10:
        replaced.append(10)
    else:
        replaced.append(val)
print("Replaced values >10:", replaced)

# 14. Fancy indexing at positions [0, 2, 4, 6]
array = [5, 10, 15, 20, 25, 30, 35]
indices = [0, 2, 4, 6]
selected = []
for i in indices:
    selected.append(array[i])
print("Fancy Indexed Elements:", selected)

# 15. Reverse a 1D array using slicing
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_array = []
for i in range(len(array) - 1, -1, -1):
    reversed_array.append(array[i])
print("Reversed Array:", reversed_array)

# ✅ Broadcasting

# 16. Add a 1x3 array to each row of a 3x3 matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_add = [10, 20, 30]
broadcast_added = []
for i in range(3):
    new_row = []
    for j in range(3):
        new_row.append(matrix[i][j] + row_add[j])
    broadcast_added.append(new_row)
print("Broadcast Row Addition:", broadcast_added)

# 17. Multiply a 1D array by scalar
array = [1, 2, 3, 4, 5]
scalar = 5
multiplied = [x * scalar for x in array]
print("Scalar Multiplication:", multiplied)

# 18. Subtract a 3x1 column vector from a 3x3 matrix
col_vector = [1, 2, 3]
subtracted = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix[i][j] - col_vector[i])
    subtracted.append(row)
print("Column Vector Subtraction:", subtracted)

# 19. Add scalar to 3D array (2x2x2)
array_3d = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
scalar_added = []
for i in range(2):
    layer = []
    for j in range(2):
        row = []
        for k in range(2):
            row.append(array_3d[i][j][k] + 5)
        layer.append(row)
    scalar_added.append(layer)
print("3D Scalar Addition:", scalar_added)

# 20. Add arrays of shape (4,1) and (1,5)
a = [[1], [2], [3], [4]]
b = [[10, 20, 30, 40, 50]]
broadcast_result = []
for i in range(4):
    row = []
    for j in range(5):
        row.append(a[i][0] + b[0][j])
    broadcast_result.append(row)
print("Broadcasted (4x1) + (1x5):", broadcast_result)

# ✅ Vectorized Operations

# 21. Square root of each element in 2D array
array2d = [[4, 9], [16, 25]]
def sqrt(x):
    r = x
    for _ in range(10):
        r = 0.5 * (r + x / r)
    return r
sqrt_applied = [[sqrt(val) for val in row] for row in array2d]
print("Manual Sqrt:", sqrt_applied)

# 22. Dot product of two 1D arrays of size 5
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
dot = 0
for i in range(5):
    dot += a[i] * b[i]
print("Dot Product:", dot)

# 23. Element-wise comparison
a = [2, 4, 6, 8, 10]
b = [1, 5, 5, 10, 9]
comparison = []
for i in range(len(a)):
    comparison.append(a[i] > b[i])
print("Comparison A > B:", comparison)

# 24. Double each element in 2D array
matrix = [[1, 2], [3, 4]]
doubled = [[val * 2 for val in row] for row in matrix]
print("Doubled Elements:", doubled)

# 25. Sum of all even numbers in 1D array
array = [random.randint(1, 100) for _ in range(100)]
sum_even = 0
for val in array:
    if val % 2 == 0:
        sum_even += val
print("Sum of Even Numbers:", sum_even)
