import pandas
from turtle import Turtle, Screen

FONT = ('Arial', 'regular', 12)

pd = pandas.read_csv("50_states.csv")
print(pd.head())
states = pd['state'].to_list()
print(states)

scr = Screen()
scr.setup(width = 725, height = 491)
scr.bgpic("blank_states_img.gif")
guess = scr.textinput(title = "Name the US states", prompt = "Name a state").title()

sd = pd[pd['state'] == guess]
if not sd.empty:
    print(sd)


    bob = Turtle()
    bob.hideturtle()
    bob.penup()
    bob.goto(sd['x'], sd['y'])
    bob.write(sd['state'], align = "center", font = FONT)




scr.exitonclick()
