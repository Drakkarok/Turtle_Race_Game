import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

colors = ["red", "orange", "pink", "green", "blue", 'purple']
turtle_names = ["timmy", "tommy", "teddy", "yenny", "filky", "pidy"]
y_positions = [-125, -75, -25, 25, 75, 125]
is_race_on = False

turtle.setup(width=1000, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

for turtle_index in range(0, 6):
    turtle_names[turtle_index] = Turtle(shape="turtle")
    turtle_names[turtle_index].color(colors[turtle_index])
    turtle_names[turtle_index].penup()
    turtle_names[turtle_index].goto(x=-470, y=y_positions[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    # random_distance = random.randint(1, 10)
    for turtle_index in range(0, 6):
        turtle_names[turtle_index].forward(random.randint(0, 10))
        if turtle_names[turtle_index].xcor() > 460:
            print(f"{turtle_names[turtle_index].pencolor()} wins!")
            if user_bet == turtle_names[turtle_index].pencolor():
                print(f"You won!")
            else:
                print(f"You lost :( ")
            is_race_on = False






####################
screen.exitonclick()