import random
from turtle import Turtle,Screen

is_race =False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make bet",prompt="which turtle will win the race? which color it is")
colors=["red","blue","green","orange","purple","yellow"]
y_position=[-70,-40,-10,20,50,80]
all_turtle=[]

for i in range(0,6):
  new_turle=Turtle(shape="turtle")
  new_turle.penup()
  new_turle.color(colors[i])
  new_turle.goto(x=-230, y=y_position[i])
  all_turtle.append(new_turle)



if user_bet:
    is_race=True

while is_race:
    for turtle in all_turtle:
        if turtle.xcor()>220:
            is_race=False
            winning_turtle=turtle.pencolor()
            if winning_turtle==user_bet:
                print("you win the race")
            else:
                print("you lost the race")
        rand_dis=random.randint(0,10)
        turtle.forward(rand_dis)


screen.exitonclick()