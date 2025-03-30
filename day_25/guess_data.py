import pandas
name = "Alaska"


class State:
    def __init__(self):


    
    
        states = pandas.read_csv("./day_25/50_states.csv")

        selected_state = states[states.state == f"{name}"]

        x = int(selected_state.x)

        y= int(selected_state.y)
