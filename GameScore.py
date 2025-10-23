from turtle import Turtle 

SCORE = 0
ALIGNMENT = 'center'
FONT = 'Arial'
FONT_SIZE = 12
FONT_TYPE = "bold"

class my_score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.game_score = SCORE
    def give_score(self):
        self.write(self.game_score, align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
    def score_increase(self):
        self.clear()
        self.game_score += 1
    def final_score(self):
        self.clear()
        self.goto(0, 0)
        FONT_SIZE = 45
        self.write(self.game_score, align="center", font=(FONT, FONT_SIZE, FONT_TYPE))