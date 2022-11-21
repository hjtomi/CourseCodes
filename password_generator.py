# Password Generator Project
import random
import time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# SOLUTION 1

# PLAN
# put all symbols into a random place in password_dictionary
# put all numbers into a random place in ...
# put all remaining letters

spaces_available = [i for i in range(nr_letters)]
pw_list = [""] * nr_letters

for _ in range(nr_symbols):
    space = random.choice(spaces_available)
    spaces_available.remove(space)

    pw_list[space] = random.choice(symbols)

for _ in range(nr_numbers):
    space = random.choice(spaces_available)
    spaces_available.remove(space)

    pw_list[space] = random.choice(numbers)

for _ in range(nr_letters-(nr_symbols+nr_numbers)):
    space = random.choice(spaces_available)
    spaces_available.remove(space)

    pw_list[space] = random.choice(letters)

pw = ""
for character in pw_list:
    pw += character

print(pw)

# SOLUTION2

# PLAN
# put in all random symbols, numbers then letters in order
# shuffle the list

pw_list2 = list()
for _ in range(nr_symbols):
    pw_list2.append(random.choice(symbols))

for _ in range(nr_numbers):
    pw_list2.append(random.choice(numbers))

for _ in range(nr_letters-(nr_symbols+nr_numbers)):
    pw_list2.append(random.choice(letters))

pw2 = ""
random.shuffle(pw_list2)
for char in pw_list2:
    pw2 += char
print(pw2)

