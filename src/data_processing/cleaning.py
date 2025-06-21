
# 1. Import CSV (simulate as list of dicts), drop rows with missing values
data = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': None},
    {'Name': None, 'Age': 30},
    {'Name': 'Carol', 'Age': 27}
]
cleaned = []
for row in data:
    if None not in row.values():
        cleaned.append(row)
print("After drop missing:", cleaned)

# 2. Replace missing numerical values with mean
age_sum = age_count = 0
for row in data:
    if row['Age'] is not None:
        age_sum += row['Age']
        age_count += 1
mean_age = age_sum / age_count
for row in data:
    if row['Age'] is None:
        row['Age'] = mean_age
print("Filled missing Age with mean:", data)

# 3. Replace missing categorical values with mode
name_counts = {}
for row in data:
    if row['Name'] is not None:
        name_counts[row['Name']] = name_counts.get(row['Name'], 0) + 1
mode_name = max(name_counts, key=name_counts.get)
for row in data:
    if row['Name'] is None:
        row['Name'] = mode_name
print("Filled missing Name with mode:", data)
