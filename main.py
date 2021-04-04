import pandas
from turtle import Turtle, Screen

pd = pandas.read_csv("50_states.csv")
print(pd.head())
states = pd['state'].to_list()
print(states)

scr = Screen()
scr.setup(width = 725, height = 491)
scr.bgpic("blank_states_img.gif")
guess = scr.textinput(title = "Name the US states", prompt = "Name a state").title()

if guess in states:
    state_data = pd['state'] == guess
    print(state_data)

bob = Turtle()
bob.hideturtle()
bob.penup()




scr.exitonclick()
