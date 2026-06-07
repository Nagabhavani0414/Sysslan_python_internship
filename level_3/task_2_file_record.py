# Save record
name = input("Enter Name: ")

file = open("records.txt", "a")
file.write(name + "\n")
file.close()

# Read records
file = open("records.txt", "r")
print("\nSaved Records:")
print(file.read())
file.close()