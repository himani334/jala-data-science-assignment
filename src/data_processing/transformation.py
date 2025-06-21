
data = [
    {'A': 10, 'B': 20},
    {'A': 15, 'B': 25},
    {'A': 30, 'B': 40}
]

# 1. Create new column as sum of A and B
for row in data:
    row['Total'] = row['A'] + row['B']

# 2. Apply sqrt to column B (manual)
def sqrt(n):
    x = n
    for _ in range(10):
        x = 0.5 * (x + n / x)
    return x
for row in data:
    row['Sqrt_B'] = sqrt(row['B'])

# 3. Normalize column A using Min-Max logic
values = [row['A'] for row in data]
min_val = min(values)
max_val = max(values)
for row in data:
    row['A_norm'] = (row['A'] - min_val) / (max_val - min_val)
print("Transformed Data:", data)

