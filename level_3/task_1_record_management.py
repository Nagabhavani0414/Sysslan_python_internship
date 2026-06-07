students = {}

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        students[name] = age

    elif choice == "2":
        print("\nStudent Records")
        for name, age in students.items():
            print(name, "-", age)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")