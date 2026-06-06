grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

number = int(input("Enter a number to search: "))

found = False

for row in grid:
    if number in row:
        found = True
        break

if found:
    print("Number found in the grid.")
else:
    print("Number not found in the grid.")