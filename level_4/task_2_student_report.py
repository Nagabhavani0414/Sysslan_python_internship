students = {
    "Rahul": 85,
    "Priya": 92,
    "Anjali": 78,
    "Kiran": 65
}

for name, marks in students.items():
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    else:
        grade = "C"

    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print("-" * 20)