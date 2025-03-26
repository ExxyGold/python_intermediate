from turtle import Turtle
start_position = [(0,0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

snake_size = 3

class Snake():
    def __init__(self):
        
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for _ in start_position:
            self.add_segment(_)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)

        self.snake.append(tim)
    
    def extend(self):
        self.add_segment(self.snake[-1].position())
        
    def reset(self):
        for segment in self.snake:
            segment.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

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

