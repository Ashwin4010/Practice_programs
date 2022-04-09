import turtle
import pandas as pd

states = pd.read_csv("50_states.csv")
all_state = states.state.to_list()
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
while len(guessed_states)<50:

    answer_state = screen.textinput(f"{len(guessed_states)}/50 states guessed correctly","Enter the Name of the state").capitalize()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv", index=None)
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


screen.exitonclick()