from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color_list = ['DeepSkyBlue4', 'DodgerBlue', 'LightSkyBlue4', 'wheat4', 'sienna', 'gray', 'firebrick']
all_plyers = []
y = 0
for i in range(0, 7):
    new_races = Turtle(shape='turtle')
    new_races.penup()
    new_races.goto(x=-240, y=-70 + y)
    y += 30
    new_races.color(color_list[i])
    all_plyers.append(new_races)
player_on_bet = screen.textinput(title="please bet on a player", prompt="enter your bet color")
player_on_bet = random.choice(color_list)


bet = True
while bet:
    for player in all_plyers:
        random_distance = random.randint(0, 10)
        player.forward(random_distance)
        if player.xcor() > 220:
            bet = False
            winner=player.pencolor()
            if player_on_bet == winner:
                print('you win')
            else:
                print('you lose')

screen.exitonclick()
