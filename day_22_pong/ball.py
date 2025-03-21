from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.05

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.penup()
        self.goto(x_cor , y_cor)

    def bounce(self):
        self.y_move *= -1

    def ped_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.ped_bounce()

