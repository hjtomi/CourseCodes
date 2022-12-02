with open("file.txt", "w") as file:
    file.write(input("what should be in the file? "))

with open("file.txt", "r") as file:
    print(file.read())
