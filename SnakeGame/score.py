from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.update_text()

    def increment_score(self):
        self.score += 1
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", font=FONT, align=ALIGNMENT)
