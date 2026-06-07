tasks = []

while True:
    task = input("Enter task (or 'exit' to stop): ")

    if task.lower() == "exit":
        break

    tasks.append(task)

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

print("Tasks saved successfully!")