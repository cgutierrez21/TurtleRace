from turtle import Turtle, Screen
import random, os
os.system("clear")


window = Screen()
window.setup(1000, 400)
window.bgcolor("grey")


colors = ["red", "blue", "green", "black", 'yellow', "orange", "purple"]
y_coor = -180
turtles = []
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-480, y_coor)
    y_coor += 60
    turtles.append(turtle)

user_guess = window.textinput("Guess the Winner","Which turtle do you think will win?\nEnter"
                    " red, blue, green, yellow, orange, purple, or black")
race_on = False

if user_guess.lower() in colors:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 480:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess.lower():
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(2, 10))








window.exitonclick()
