from turtle import Turtle, Screen

timmy = Turtle()

def move_forward():
    timmy.forward(50)

screen = Screen()
screen.listen()
screen.onkey(key = "space", fun = move_forward)
screen.exitonclick()