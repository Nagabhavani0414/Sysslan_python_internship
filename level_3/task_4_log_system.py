from datetime import datetime

message = input("Enter log message: ")

with open("log.txt", "a") as file:
    file.write(f"{datetime.now()} - {message}\n")

print("Log saved successfully!")