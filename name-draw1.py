import turtle
import random

# Let's create our turtle and call him Simon!
simon = turtle.Turtle()

# We'll set the background to black
turtle.bgcolor("black")

# This is our list of colours
colors = ["red", "green", "blue"]

# We need to ask the user their name
name = turtle.textinput("Name", "What is your name?")

simon.penup()

for number in range(30): # We'll draw the name 30 times
    simon.forward(number * 10)
    simon.write(name, font=("Arial", 12, "bold")) # This writes the name and chooses a font
    simon.right(92)
    simon.pencolor(random.choice(colors)) # This chooses a random colour
