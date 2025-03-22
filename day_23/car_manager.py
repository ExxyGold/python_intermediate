from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        probability =  random.randint(1, 6)
        if probability == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid= 1, stretch_len=2 )
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.carspeed)
    
    def speed_up(self):
        self.carspeed += MOVE_INCREMENT 

        
        
