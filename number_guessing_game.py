# Create a random number between 1 and 100
# ask for difficulty
# set attempts
# ask for a guess
# display if it was too high or too low
# if the guess is the chosen number, display something funky
import random

attempts = 0
query = random.randint(1, 100)
difficulty = ""
while difficulty != "e" and difficulty != "h":
    difficulty = input("Easy or hard difficulty? (e/h)\n")
    if difficulty == "e":
        attempts = 10
        print("You have 10 attempts")
    elif difficulty == "h":
        attempts = 5
        print("You have 5 attempts")

while attempts > 0:
    guess = int(input("Make a guess!\n"))
    if guess > query:
        print("Too high!")
    elif guess < query:
        print("Too low!")
    else:
        print("You guessed it, bravo!")
        break
    attempts -= 1
    print(f"You have {attempts} attempts left...")
