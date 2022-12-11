def addition(*args):
    return sum(args)


print(addition(4, 5, 6, 7, 2, 3, 5, 6, 568, 978, 567, 456, 567, 345))

import tkinter

screen = tkinter.Tk()

# # Course example
# screen.config(padx=50, pady=50)
#
# my_label = tkinter.Label(screen, text="Label")
# my_button = tkinter.Button(screen, text="Button")
# my_new_button = tkinter.Button(screen, text="New Button")
# my_entry = tkinter.Entry(screen)
#
# my_label.grid(row=0, column=0)
# my_button.grid(row=1, column=1)
# my_new_button.grid(row=0, column=2)
# my_entry.grid(row=2, column=3)


# Coding Challenge Miles to Km converter
# consists of: 1 entry, 4 labels, 1 button

screen.config(padx=18, pady=18)


def calculate():
    num = float(entry.get())
    label_number.config(text=num*1.609)


entry = tkinter.Entry(screen, width=10)
button = tkinter.Button(screen, text="Calculate", command=calculate)
label_miles = tkinter.Label(screen, text="Miles")
label_is_equal_to = tkinter.Label(screen, text="is equal to")
label_number = tkinter.Label(screen, padx=10, pady=5)
label_km = tkinter.Label(screen, text="Km")

entry.grid(row=0, column=1)
button.grid(row=2, column=1)
label_miles.grid(row=0, column=2)
label_is_equal_to.grid(row=1, column=0)
label_number.grid(row=1, column=1)
label_km.grid(row=1, column=2)

screen.mainloop()
