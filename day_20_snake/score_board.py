from turtle import Turtle, Screen

FONT = ("Arial", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.new_score()

    def new_score(self):
        self.write(f"Score: {self.value}", align ="center", font = FONT)

    def increase(self):
        self.value += 1
        self.clear()
        self.new_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align ="center", font = FONT)
    
        






        

