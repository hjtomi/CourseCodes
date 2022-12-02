from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
# .\ is SnakeGame, ..\ is Course, ..\..\ is Python, ..\..\..\ is Scripts, ..\..\..\..\ is D:
FILE_PATH = "..\..\..\..\Dokumentumok\Desktop\data.txt"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open(FILE_PATH, "r") as file:
            self.highscore = int(file.read())
        self.update_text()

    def increment_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            with open(FILE_PATH, "w") as file:
                file.write(str(self.highscore))
        self.update_text()

    def update_text(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} High score: {self.highscore}", font=FONT, align=ALIGNMENT)
