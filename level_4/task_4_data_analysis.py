with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)

print("Total:", total)
print("Average:", average)
print("Maximum:", maximum)