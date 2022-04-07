import turtle
import pandas as pd

states = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput("Guess The state","Enter the Name of the state").capitalize()
print(answer_state)

