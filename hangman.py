import random

word_list = ["hello", "world", "maybe"]

chosen_world = random.choice(word_list)
blank_word = ["_"] * len(chosen_world)

print(''.join(blank_word))

letters_guessed = []
life = 6
guess = ""
while True:
    guess = input("guess a letter: ").lower()
    if guess in letters_guessed:
        print(f"You have already guessed '{guess}'")
    elif guess in chosen_world:
        letters_guessed.append(guess)
        for i, letter in enumerate(chosen_world):
            if letter == guess:
                blank_word[i] = guess
    else:
        print("letter not in word\n")
        life -= 1

    print(''.join(blank_word) + f"\nLives left: {life}")

    if ''.join(blank_word) == chosen_world:
        print("You won!")
        break

    if life < 1:
        print(f"Game over!\nThe word was '{chosen_world}' ")
        break

