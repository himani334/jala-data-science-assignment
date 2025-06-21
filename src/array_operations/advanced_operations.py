import random

matrix_5x5 = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
value_to_replace = 5
replacement_value = 99
replaced_matrix = []
for row in matrix_5x5:
    replaced_row = []
    for val in row:
        if val == value_to_replace:
            replaced_row.append(replacement_value)
        else:
            replaced_row.append(val)
    replaced_matrix.append(replaced_row)
print("Original Matrix:", matrix_5x5)
print("Replaced Matrix:", replaced_matrix)

# --- Cross product of two 3-element vectors ---
def cross_product(u, v):
    return [
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0]
    ]
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]
cross = cross_product(vec1, vec2)
print("Cross Product:", cross)

# --- Find unique elements in a random integer array ---
array = [random.randint(1, 10) for _ in range(20)]
unique = []
for val in array:
    if val not in unique:
        unique.append(val)
print("Original Array:", array)
print("Unique Elements:", unique)
