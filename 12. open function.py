"""
name = input("Name: ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line, end="")
    # OR print(line.rstrip())