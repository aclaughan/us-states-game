from turtle import Screen, Turtle

import pandas
import logging

# logging.basicConfig(level=logging.INFO)

pd = pandas.read_csv("50_states.csv")
logging.info(f'pd.head : \n  {pd.head()}')
states = pd.state.to_list()
logging.info(f'states : \n  {states}')

scr = Screen()
scr.title("US States Game")
scr.setup(width = 725, height = 491)
scr.bgpic("blank_states_img.gif")
guessed_states = []

while len(guessed_states) < 50:
    guess = scr.textinput(title = f"{len(guessed_states)}/50 states found",
                          prompt = "Guess a state").title()

    if guess == 'Quit':
        break

    if guess in states:
        bob = Turtle()
        bob.hideturtle()
        bob.penup()
        sd = pd[pd.state == guess]
        bob.goto(int(sd.x), int(sd.y))
        bob.write(sd.state.item(), align = "center")
        guessed_states.append(guess)

states_to_learn = []

for state in states:
    if state not in guessed_states:
        states_to_learn.append(state)

new_df = pandas.DataFrame(states_to_learn)
new_df.to_csv("states_to_learn.csv")

logging.info(f'{len(states_to_learn)} missed : \n  {states_to_learn}')
