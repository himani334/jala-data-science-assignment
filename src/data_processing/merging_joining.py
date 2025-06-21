

# Simulate 2 datasets
data1 = [
    {'ID': 1, 'Name': 'Alice'},
    {'ID': 2, 'Name': 'Bob'}
]
data2 = [
    {'ID': 1, 'Score': 85},
    {'ID': 3, 'Score': 90}
]

# 1. Merge on 'ID' (inner join)
merged = []
for row1 in data1:
    for row2 in data2:
        if row1['ID'] == row2['ID']:
            merged.append({**row1, **row2})
print("Merged Data:", merged)

# 2. Left join
data_left_join = []
for row1 in data1:
    matched = False
    for row2 in data2:
        if row1['ID'] == row2['ID']:
            data_left_join.append({**row1, **row2})
            matched = True
            break
    if not matched:
        data_left_join.append({**row1, 'Score': None})
print("Left Join:", data_left_join)

# 3. Concatenate column-wise
data_a = [{'X': 1}, {'X': 2}]
data_b = [{'Y': 3}, {'Y': 4}]
concat = []
for i in range(len(data_a)):
    combined = {**data_a[i], **data_b[i]}
    concat.append(combined)
print("Concatenated:", concat)
