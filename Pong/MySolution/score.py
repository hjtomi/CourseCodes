from turtle import Turtle

PLAYER_SCORE_POS = -50
AI_SCORE_POS = 50
SCORE_Y = 190

FONT = ("Ariel", 75, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()

        self.player_score = 0
        self.ai_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        # Player
        self.goto(PLAYER_SCORE_POS, SCORE_Y)
        self.write(str(self.player_score), align="center", font=FONT)

        # ai
        self.goto(AI_SCORE_POS, SCORE_Y)
        self.write(str(self.ai_score), align="center", font=FONT)

