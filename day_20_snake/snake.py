from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        x= 0
        for _ in range(3):
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(x , 0 )
            x -= 20
            self.snake.append(tim)


    def move(self):
        movement = 20
        for seg in range(len(self.snake)-1, 0,  -1):
            x = self.snake[seg-1].xcor()
            y = self.snake[seg-1].ycor()
            self.snake[seg].goto(x, y)
        self.head.forward(movement)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

