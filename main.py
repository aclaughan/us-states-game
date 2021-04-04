from turtle import Screen, Turtle

import pandas

FONT = ('Arial', 'regular', 12)

pd = pandas.read_csv("50_states.csv")
print(pd.head())
states = pd.state.to_list()
print(states)

scr = Screen()
scr.title("US States Game")
scr.setup(width = 725, height = 491)
scr.bgpic("blank_states_img.gif")
guessed_states = []

while len(guessed_states) < 50:
    guess = scr.textinput(title = f"{len(guessed_states)}/50 states found",
                          prompt = "Guess a state").title()

    if guess in states:
        bob = Turtle()
        bob.hideturtle()
        bob.penup()
        sd = pd[pd.state == guess]
        bob.goto(int(sd.x), int(sd.y))
        bob.write(sd.state.item(), align = "center")
        guessed_states.append(guess)

scr.exitonclick()
