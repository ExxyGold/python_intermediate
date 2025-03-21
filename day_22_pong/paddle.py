from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
    
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=  1, stretch_len = 5)
        self.penup()
        self.goto(coordinate)
        self.setheading(90)

    def upward(self):
        self.forward(20)

    def downward(self):
        self.back(20)


