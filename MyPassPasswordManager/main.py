from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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

    # Prepare for JSON
    new_data = {
        website: {
            "Email/Username": email_username,
            "Password": password
        }
    }

    if website and email_username and password:
        try:
            with open("passwords.json", "r") as data_file:
                # Assign old data
                data = json.load(data_file)

                # Update old data with new
                data.update(new_data)

        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                # Save first data in the file
                json.dump(new_data, data_file, indent=4)

        else:
            with open("passwords.json", "w") as data_file:
                # Save updated data
                json.dump(data, data_file, indent=4)

        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)
    else:
        messagebox.showerror(title="Error!", message="Please fill everything")


# ---------------------------- FIND DATA ---------------------------------#


def find_password():
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found")

    else:
        desired_page = entry_website.get()
        if desired_page in data:
            desired_page_email = data[desired_page]["Email/Username"]
            desired_page_password = data[desired_page]["Password"]

            messagebox.showinfo(title=desired_page,
                                message=f"email: {desired_page_email}\npassword: {desired_page_password}")

        else:
            messagebox.showerror(title="Error", message=f"No data registered to '{desired_page}' website")


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
entry_website = Entry(window, width=32)
entry_website.focus()
entry_email_username = Entry(window, width=52)
entry_email_username.insert(0, "hjtomipls@gmail.com")
entry_password = Entry(window, width=32)

# Buttons
button_generate = Button(window, text="Generate Password", command=generate_password)
button_add = Button(window, text="Add", width=34, command=save_data)
button_search = Button(window, text="Search", width=14, command=find_password)


canvas.grid(row=0, column=1)

label_website.grid(row=1, column=0)
label_email_username.grid(row=2, column=0)
label_password.grid(row=3, column=0)

entry_website.grid(row=1, column=1)
entry_email_username.grid(row=2, column=1, columnspan=2, sticky="w")
entry_password.grid(row=3, column=1, sticky="w")

button_generate.grid(row=3, column=2, sticky="w")
button_add.grid(row=4, column=1, columnspan=2, sticky="w")
button_search.grid(row=1, column=2)

window.mainloop()
