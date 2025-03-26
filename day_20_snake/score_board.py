from turtle import Turtle, Screen

FONT = ("Arial", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        with open("data.txt") as file:
            content = file.read()
        self.highscore = int(content)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.new_score()

    def new_score(self):
        self.clear()
        self.write(f"Score: {self.value} Highscore = {self.highscore}", align ="center", font = FONT)

    def increase(self):
        self.value += 1
        self.new_score()

    def reset_score(self):
        if self.value> self.highscore:
            with open("data.txt", mode = "w") as file:
                file.write(str(self.value))
            with open("data.txt") as file:
                self.highscore = int(file.read())
        self.value = 0
        self.new_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align ="center", font = FONT)
    
        






        

