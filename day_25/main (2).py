import turtle
import pandas


screen = turtle.Screen()


screen.title("U.S. States Game")

image = "./day_25/blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

state_data = pandas.read_csv("./day_25/50_states.csv")
states = state_data.state
states_list = states.tolist()

correct_answer = []

TITLE = "Guess the states"


while len(correct_answer)< 50:
    
    answer_state = screen.textinput(  title = TITLE, prompt= "What's another state's name?").title()

    if answer_state in states_list:
        correct_answer.append(answer_state)
        TITLE = F"{len(correct_answer)}/50 States Correct"
        selected_state = state_data[state_data.state == f"{answer_state}"]
        

        pos_x = int(selected_state.x.item())
        pos_y = int(selected_state.y.item())

        guess = turtle.Turtle()
        guess.hideturtle()
        guess.penup()
        guess.goto(pos_x, pos_y)
        guess.write(f"{answer_state}", align = "center", font = ("Arial", 8, "normal"))
        
    if answer_state == "Exit":
        break


missed_data = [answers for answers in states_list if answers not in correct_answer]



missed_dataframe = pandas.DataFrame(missed_data)



missed_dataframe.to_csv("./day_25/states_to_learn.csv")
