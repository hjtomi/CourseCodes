import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# {new_key: new_value for index, row in DataFrame.iterrows()}
letter_dictionary = {row.letter: row.code for index, row in data.iterrows()}

name = ""
while name != "exit":
    name = input("Enter your name: ").upper()

    name_in_code_list = [letter_dictionary[letter] for letter in name]
    print(name_in_code_list)
