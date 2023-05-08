from tkinter import *
import quotes
import random


def new_quote():
    global quote, quote_words, current_word_num
    quote = quotes[random.randint(1, 3)]
    quote_words = quote.split()

    quote_label.config(text=quote)


def key_pressed(event):
    global current_word_num, total_typed
    typed = entry.get()

    # Last word typed
    if current_word_num + 1 == len(quote_words) and typed == quote_words[current_word_num]:
        entry.delete(0, END)
        current_word_num = 0

        total_typed += len(quote_words[current_word_num])

        new_quote()

    # Word typed
    if typed == quote_words[current_word_num] + ' ':
        entry.delete(0, END)
        current_word_num += 1

        total_typed += len(quote_words[current_word_num] + ' ')


def update_wpm():
    global seconds
    seconds += 0.5
    wpm = round((total_typed / 5) / (seconds / 60))
    wpm_label.config(text=f'WPM: {wpm}')

    window.after(500, update_wpm)


quotes = quotes.quotes
quote = ''
quote_words = []
current_word_num = 0

total_typed = 0
seconds = 0

window = Tk()
window.title('Typing Speed App')
window.bind("<KeyPress>", key_pressed)
window.after(500, update_wpm)

quote_label = Label(text=quote, font=50)
wpm_label = Label(text='WPN: 0', font=10)
entry = Entry(font=50, width=10)

wpm_label.pack()
quote_label.pack()
entry.pack()
entry.focus_set()

new_quote()

window.mainloop()
