from turtle import Turtle

FONT = ("Arial", 80, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 190)
        self.l_score = 0
        self.r_score = 0
        self.score_write()

    def score_write(self):
        self.write(f"{self.l_score} : {self.r_score}", align = "center", font = FONT )

    def increase_l(self):
        self.clear()
        self.l_score += 1
        self.score_write()

    def increase_r(self):
        self.clear()
        self.r_score += 1
        self.score_write()