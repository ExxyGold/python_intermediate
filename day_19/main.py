from turtle import Turtle, Screen

timmy = Turtle()

def move_forward():
    timmy.forward(10)
def left():
    timmy.left(10)
def right():
    timmy.right(10)
def back():
    timmy.backward(10)
def clear():
    timmy.clear()


screen = Screen()
screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "a", fun = left )
screen.onkey(key = "d", fun = right)
screen.onkey(key = "s", fun = back)
screen.onkey(key= "c", fun = clear)
screen.exitonclick()