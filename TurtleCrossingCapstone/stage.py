from turtle import Turtle


class Stage(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.stage = 1
        self.write_stage()

    def write_stage(self):
        self.clear()
        self.goto(-290, 265)
        self.write(f"Level {self.stage}", False, "left", ("Courier", 20, "normal"))

    def stage_up(self):
        self.stage += 1
        self.write_stage()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, "center", ("Courier", 50, "normal"))
