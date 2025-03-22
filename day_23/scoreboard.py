from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.create_score()
        


    def create_score(self):
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.create_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = "center", font = FONT)

