from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False


    def start_over(self):
        self.create_turtle()
