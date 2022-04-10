import turtle
import pandas as pd

states = pd.read_csv("countries.csv")
all_state = states.country.to_list()
guessed_states = []

screen = turtle.Screen()
screen.title("Countries")
image = "map.gif"
screen.addshape(image)
turtle.shape(image)
while len(guessed_states)<50:

    answer_state = screen.textinput(f"{len(guessed_states)}/194 states guessed correctly","Enter the Name of the state").capitalize()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for country in all_state:
            if country not in guessed_states:
                missing_states.append(country)
        print(missing_states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("countries_to_learn.csv", index=None)
        break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.country == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


screen.exitonclick()