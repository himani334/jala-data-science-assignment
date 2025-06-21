# 1. Group by category and compute mean & std
sales_data = [
    {'Category': 'Electronics', 'Amount': 100},
    {'Category': 'Clothing', 'Amount': 50},
    {'Category': 'Electronics', 'Amount': 150},
    {'Category': 'Clothing', 'Amount': 70},
    {'Category': 'Books', 'Amount': 30}
]

# Grouping
grouped = {}
for row in sales_data:
    cat = row['Category']
    if cat not in grouped:
        grouped[cat] = []
    grouped[cat].append(row['Amount'])

# Compute mean and std dev
results = {}
for cat, amounts in grouped.items():
    total = sum(amounts)
    count = len(amounts)
    mean = total / count
    variance = sum([(x - mean) ** 2 for x in amounts]) / count
    std_dev = variance ** 0.5
    results[cat] = {'mean': mean, 'std_dev': std_dev}
print("Group-wise Stats:", results)

# 2. groupby sum and apply function (square)
sales_data = [
    {'Category': 'Books', 'Sales': 10},
    {'Category': 'Books', 'Sales': 15},
    {'Category': 'Stationery', 'Sales': 5},
    {'Category': 'Stationery', 'Sales': 7}
]

# Group and sum
sum_group = {}
for row in sales_data:
    cat = row['Category']
    if cat not in sum_group:
        sum_group[cat] = 0
    sum_group[cat] += row['Sales']

# Apply function (square)
transformed = {k: v ** 2 for k, v in sum_group.items()}
print("Squared Group Sums:", transformed)

# 3. Pivot table from grouped data
pivot_data = [
    {'Region': 'North', 'Type': 'Retail', 'Revenue': 100},
    {'Region': 'North', 'Type': 'Wholesale', 'Revenue': 200},
    {'Region': 'South', 'Type': 'Retail', 'Revenue': 150},
    {'Region': 'South', 'Type': 'Wholesale', 'Revenue': 250}
]

pivot_table = {}
for row in pivot_data:
    key = (row['Region'], row['Type'])
    if key not in pivot_table:
        pivot_table[key] = 0
    pivot_table[key] += row['Revenue']
print("Pivot Table:", pivot_table)

# --- Array Operations on DataFrame Columns ---
data = [
    {'X': 10}, {'X': 20}, {'X': 30}
]

# 1. Element-wise square
x_array = [row['X'] for row in data]
squared = [x * x for x in x_array]
print("Squared Values:", squared)

# 2. Reshape and assign
flat_array = [1, 2, 3, 4, 5, 6]
reshaped = []
for i in range(0, len(flat_array), 2):
    reshaped.append(flat_array[i:i+2])
for i in range(len(data)):
    data[i]['NewCol'] = reshaped[i]
print("Reshaped Assignment:", data)

# 3. Filter rows where X > 15
filtered = [row for row in data if row['X'] > 15]
print("Filtered Rows:", filtered)

# --- Broadcasting and Vectorized Ops ---

# 4. Broadcast array to column addition
base = [1, 2, 3]
broadcasted = [data[i]['X'] + base[i] for i in range(len(data))]
print("Broadcasted Addition:", broadcasted)

# 5. Vectorized sum of multiple columns
multi_col_data = [
    {'A': 1, 'B': 2},
    {'A': 3, 'B': 4},
    {'A': 5, 'B': 6}
]
for row in multi_col_data:
    row['Sum'] = row['A'] + row['B']
print("Column-wise Sums:", multi_col_data)

# 6. Subtract row mean from each element
adjusted = []
for row in multi_col_data:
    vals = [row['A'], row['B'], row['Sum']]
    mean = sum(vals) / len(vals)
    adjusted_row = [v - mean for v in vals]
    adjusted.append(adjusted_row)
print("Row Mean Adjusted:", adjusted)
# --- Linear Algebra with DataFrame-style input ---

# 7. Solve system of equations: Ax = B
A = [[2, 3], [1, -2]]
B = [8, -3]

def solve_2x2(A, B):
    a, b = A[0]
    c, d = A[1]
    det = a * d - b * c
    if det == 0:
        return None
    x = (B[0]*d - b*B[1]) / det
    y = (a*B[1] - B[0]*c) / det
    return [x, y]

solution = solve_2x2(A, B)
print("Linear System Solution:", solution)

# 8. Dot product of two columns
dot_data = [
    {'U': 2, 'V': 5},
    {'U': 3, 'V': 4},
    {'U': 1, 'V': 6}
]
dot_product = 0
for row in dot_data:
    dot_product += row['U'] * row['V']
print("Dot Product:", dot_product)

# 9. Matrix multiplication between two datasets
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
result = []
for i in range(len(mat1)):
    row = []
    for j in range(len(mat2[0])):
        cell = 0
        for k in range(len(mat2)):
            cell += mat1[i][k] * mat2[k][j]
        row.append(cell)
    result.append(row)
print("Matrix Multiplication Result:", result)
# --- Time Series Analysis (Manual) ---

# 10. Create timestamps and calculate time difference
log_data = [
    {'event': 'start', 'time': '2023-06-01 10:00:00'},
    {'event': 'middle', 'time': '2023-06-01 10:15:30'},
    {'event': 'end', 'time': '2023-06-01 11:00:00'}
]

# Convert time to seconds since midnight (simplified parser)
def time_to_seconds(t):
    date, clock = t.split()
    h, m, s = map(int, clock.split(':'))
    return h * 3600 + m * 60 + s

for row in log_data:
    row['timestamp'] = time_to_seconds(row['time'])

# Compute time differences in seconds
for i in range(1, len(log_data)):
    diff = log_data[i]['timestamp'] - log_data[i-1]['timestamp']
    log_data[i]['time_diff_sec'] = diff
print("Log with Time Differences:", log_data)

# 11. Rolling average over window size 2
values = [10, 20, 30, 40, 50]
window = 2
rolling_avg = []
for i in range(len(values)):
    if i < window - 1:
        rolling_avg.append(None)
    else:
        avg = sum(values[i - window + 1:i + 1]) / window
        rolling_avg.append(avg)
print("Rolling Average (2):", rolling_avg)

# 12. Identify max value timestamp in time series
temp_series = [
    {'time': '08:00:00', 'temp': 29},
    {'time': '10:00:00', 'temp': 33},
    {'time': '12:00:00', 'temp': 37},
    {'time': '14:00:00', 'temp': 35}
]
max_temp = -1
max_time = ''
for row in temp_series:
    if row['temp'] > max_temp:
        max_temp = row['temp']
        max_time = row['time']
print("Max Temp Timestamp:", max_time, "Temp:", max_temp)