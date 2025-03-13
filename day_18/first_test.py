from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
tim.speed("fastest")
def rand_color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1, 255)
    return(r, g, b)



# tim.shape("turtle")




colour = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "black", "brown"]



tim.circle(100)

def draw(direction):
    tim.setheading(direction)
    tim.circle(100)
bearing = 0
for _ in range (0, 60):
    tim.color(rand_color())
    draw(bearing)
    bearing += 6


# def direction(face, colour):
#     tim.color(colour)
#     tim.setheading(face)
#     tim.forward(30)

# for _ in range (200):
#     chosen_direction = random.choice(bearing)
#     direction(chosen_direction, rand_color())    

# def draw(sides):
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(360/sides)
    
# for _ in range(3,11):
#     tim.color(colour[num_sides - 3])
#     draw(num_sides)
#     num_sides += 1


screen = Screen()
screen.exitonclick()
