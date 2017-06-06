# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: create a new turtle, we'll call him simon
simon = turtle.Turtle()

# Lets draw a square!
for loop in range(4):
    simon.forward(200)
    simon.left(90)
