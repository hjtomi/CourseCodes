from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()

    if website and email_username and password:

        is_ok = messagebox.askokcancel(title="Confirm", message="Are you sure you want to save?")
        if is_ok:
            with open("passwords.txt", "a") as data_file:
                data_file.write(f"{website},{email_username},{password}\n")

                entry_website.delete(0, END)
                entry_password.delete(0, END)
    else:
        messagebox.showerror(title="Error!", message="Please fill everything")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)

# Canvas
canvas = Canvas(window, width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)

# Labels
label_website = Label(window, text="Website:")
label_email_username = Label(window, text="Email/Username:")
label_password = Label(window, text="Password:")

# Entries
entry_website = Entry(window, width=52)
entry_website.focus()
entry_email_username = Entry(window, width=52)
entry_email_username.insert(0, "hjtomipls@gmail.com")
entry_password = Entry(window, width=32)

# Buttons
button_generate = Button(window, text="Generate Password", command=generate_password)
button_add = Button(window, text="Add", width=34, command=save_data)


canvas.grid(row=0, column=1)

label_website.grid(row=1, column=0)
label_email_username.grid(row=2, column=0)
label_password.grid(row=3, column=0)

entry_website.grid(row=1, column=1, columnspan=2, sticky="w")
entry_email_username.grid(row=2, column=1, columnspan=2, sticky="w")
entry_password.grid(row=3, column=1, sticky="w")

button_generate.grid(row=3, column=2, sticky="w")
button_add.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
