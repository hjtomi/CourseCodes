from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
MOTHER_FILE = "data/french_words.csv"

# get the words from the words_to_learn.csv file
# if the file does not exist yet, create it all the words from the french_words.csv
# when the "words" dictionary updates, update the words_to_learn.csv file too
try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    # Copy all words from mother file
    with open(MOTHER_FILE) as file:
        data = file.read()

    # paste all the words to a newly created csv
    with open("data/words_to_learn.csv", "w") as file:
        file.write(data)

    # get the data from the new csv
    data = pandas.read_csv("data/words_to_learn.csv")

finally:
    words = {french: english for french, english in data.values}

current_english_word = ""
current_french_word = ""

countdown = None


def new_word():
    '''Shows a new card'''

    # checks if a countdown is going (bugfix purpose)
    global countdown
    if countdown:
        window.after_cancel(countdown)

    # UI work
    canvas.itemconfig(canvas_lang, text="French")
    canvas.itemconfig(canvas_card, image=img_card_front)
    canvas.itemconfig(canvas_lang, fill="black")
    canvas.itemconfig(canvas_word, fill="black")

    # chooses a new word and assigns it
    if len(words) > 0:
        global current_french_word
        current_french_word = random.choice(list(words.keys()))

        # UI work
        canvas.itemconfig(canvas_word, text=current_french_word)

        # starts the countdown to turn the card
        countdown = window.after(3000, flip_card)

    else:
        canvas.itemconfig(canvas_lang, text="CONGRATS!\nYou learned it all")
        canvas.itemconfig(canvas_word, text="")


def flip_card():
    '''Flips the card'''

    # UI work
    canvas.itemconfig(canvas_lang, text="English")
    canvas.itemconfig(canvas_card, image=img_card_back)
    canvas.itemconfig(canvas_lang, fill="white")
    canvas.itemconfig(canvas_word, fill="white")

    global current_english_word, current_french_word
    current_english_word = words[current_french_word]
    # UI work
    canvas.itemconfig(canvas_word, text=current_english_word)


def remove_word():
    '''Remove a word from the words_to_learn file'''

    # if there is still something left in "words"
    if len(words) > 0:
        # delete the current word from the "words" dict
        del words[current_french_word]

        # empty the words_to_learn file
        with open("data/words_to_learn.csv", "w"):
            pass

        # write the words_to_learn file according to the words in "words" dict
        with open("data/words_to_learn.csv", "a", encoding='UTF-8') as file:
            file.write("French,English\n")
            for french, english in words.items():
                file.write(f"{french},{english}\n")

        new_word()


window = Tk()
window.title("FlashCard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


img_card_front = PhotoImage(file="images/card_front.png")
img_card_back = PhotoImage(file="images/card_back.png")
img_wrong = PhotoImage(file="images/wrong.png")
img_right = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_card = canvas.create_image(400, 263, image=img_card_front)
canvas_lang = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 265, font=("Ariel", 60, "bold"))

button_wrong = Button(image=img_wrong, highlightthickness=0, command=new_word)
button_right = Button(image=img_right, highlightthickness=0, command=remove_word)

canvas.grid(row=0, column=0, columnspan=2)
button_wrong.grid(row=1, column=0)
button_right.grid(row=1, column=1)

new_word()

window.mainloop()
