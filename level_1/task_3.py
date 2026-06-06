grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Row Sums:")

for i in range(len(grid)):
    row_sum = sum(grid[i])
    print(f"Row {i+1} Sum = {row_sum}")