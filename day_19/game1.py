from turtle import Turtle, Screen
import random



screen= Screen()
screen.setup(width= 500, height = 400)
user_bet = screen.textinput(title= "Make your bet", prompt = "Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = -100

race_on = False
all_turtles = []
for turtles in range(6):
    tim = Turtle()
    tim.color(colors[turtles])
    tim.shape("turtle")
    tim.penup()
    tim.goto(-240, position)
    position += 40
    all_turtles.append(tim)
    
if user_bet:
    race_on = True

while race_on:
    

    for tim in all_turtles:

        if tim.xcor() > 230 :
            race_on = False
            winner = tim.pencolor()
            if winner == user_bet:
                print(f"You won, The {winner} crossed the finish line first")
            else:
                print(f"You Lost, the {winner} crossed the finish line first")
            
        move = random.randint(1,10)
        tim.forward(move)

    

screen.exitonclick()