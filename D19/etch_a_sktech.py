import turtle as t

tim = t.Turtle()
screen = t.Screen()

tim.speed(0)


def move_forward():
    tim.forward(10)


def move_back():
    tim.back(10)


def turn_left():
    tim.left(15)


def turn_right():
    tim.right(15)


def clear_screen():
    t.resetscreen()


screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_back, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear_screen, "c")
screen.exitonclick()

