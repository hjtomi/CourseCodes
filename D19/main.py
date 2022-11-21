import turtle as t

tim = t.Turtle()
screen = t.Screen()

tim.speed(0)


def move_forward():
    tim.forward(10)


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.exitonclick()
