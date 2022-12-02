# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# for each name
# create a new empty file
# copy the starting_letter's contents to it
# change the [name] to the actual name

names = []
with open("./Input/Names/invited_names.txt") as names_file:
    for line in names_file.readlines():
        names.append(line.rstrip())

with open("./Input/Letters/starting_letter.txt") as raw_letter_file:
    raw_letter = raw_letter_file.read()

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as new_file:
        new_file.write(raw_letter.replace("[name]", name))

