from turtle import Turtle, Screen, colormode
import random
timmy = Turtle()
colormode(255)
timmy.hideturtle()
timmy.penup()
timmy.setposition(-250, -200)
colour_list = [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)]


def move():
    timmy.pencolor(random.choice(colour_list))
    timmy.dot(20)
    timmy.forward(50)
 
def row():
    for _ in range(10):
        move()

vertical = -200
for _ in range (10):
    row()
    vertical += 50
    timmy.goto(-250, vertical)
    



screen = Screen()
screen.exitonclick()