import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()
writing_turtle.penup()

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(f"{len(guessed_states)}/50 states correct", "What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in states:
        # a data DataFrameben az a Series amiben a state = a válasszal
        x = data[data.state == answer_state].x
        y = data[data.state == answer_state].y
        writing_turtle.goto(int(x), int(y))
        writing_turtle.write(answer_state)
        guessed_states.append(answer_state)

states_to_learn = [state for state in states if state not in guessed_states]
df = pandas.DataFrame(states_to_learn)
df.to_csv("StatesToLearn.csv")

