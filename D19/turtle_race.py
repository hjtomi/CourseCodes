import random
import turtle as t

screen = t.Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
colors_hun_to_english_dict = {
    "piros": "red",
    "narancs": "orange",
    "sárga": "yellow",
    "zöld": "green",
    "kék": "blue",
    "lila": "purple"
}
lowest_turtle_start_y = -100

# so each new turtle starts above the previous
position_correction = 0
turtles = []
for i in range(6):
    turtle = t.Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-230, lowest_turtle_start_y + position_correction)
    turtles.append(turtle)

    position_correction += 40

player_count = int(screen.numinput(title="Hányan fogtok tippelni?", prompt="Játékosok száma:"))

names = []
english_bets = []
for i in range(player_count):
    name = screen.textinput(title="Hogy hívnak?", prompt=f"Játékos{i+1} add meg a neved!")
    names.append(name)
    bet_hun = screen.textinput(title="Add meg a voksod!", prompt="Melyik színű teknős fog leghamarabb célba érni?")
    bet_english = colors_hun_to_english_dict[bet_hun.lower()]
    english_bets.append(bet_english)

is_race_on = False
if bet_english:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color_english = turtle.pencolor()
            break

winner_names = []
for i, bet in enumerate(english_bets):
    if bet == winning_color_english:
        winner_names.append(names[i])

if len(winner_names) > 1:
    print(f"Gratulálok {winner_names} ti nyertél!")
elif len(winner_names) > 0:
    print(f"Gratulálok {winner_names} te nyertél!")
else:
    print("Senki sem nyert...")

# reverses the working of python dictionary, gets key by value
winning_color_hun = list(colors_hun_to_english_dict.keys())[list(colors_hun_to_english_dict.values()).index(winning_color_english)]
print(f"A nyerő szín a {winning_color_hun} volt.")

screen.exitonclick()

